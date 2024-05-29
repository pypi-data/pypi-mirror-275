import subprocess
import socket
import platform
import re
import logging

class Client:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def __repr__(self):
        return f"Client(name={self.name}, ip={self.ip})"

class NetworkScanner:
    def __init__(self, network_range="192.168.1.0/24"):
        """
        Initialize the NetworkScanner with the network range.

        Args:
            network_range (str): The network range to scan for clients (used in Linux). Default is "192.168.1.0/24".
        """
        self.network_range = network_range
        self.system = platform.system().lower()

    def discover_clients(self):
        """
        Discover all visible clients in the local network.

        Returns:
            list of Client: A list of Client objects for each visible client.
        """
        if self.system == 'windows':
            command = 'net view'
            parser = self._parse_windows_output
        elif self.system == 'linux':
            command = f'nmap -sn {self.network_range}'
            parser = self._parse_linux_output
        else:
            raise NotImplementedError("Unsupported platform")

        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            clients = parser(result.stdout)
        except subprocess.CalledProcessError as e:
            logging.error(f"An error occurred while running the command: {e}")
            clients = []

        return clients

    def _parse_windows_output(self, output):
        """
        Parse the output of the 'net view' command.

        Args:
            output (str): The command output as a string.

        Returns:
            list of Client: Parsed client information with 'name' and 'ip' keys.
        """
        clients = []
        lines = output.splitlines()
        for line in lines[3:]:
            if line.startswith('\\'):
                match = re.match(r'\\\\([^ ]+)', line)
                if match:
                    host_name = match.group(1)
                    ip_address = self._resolve_hostname_to_ip(host_name)
                    clients.append(Client(name=host_name, ip=ip_address))
        return clients

    def _parse_linux_output(self, output):
        """
        Parse the output of the 'nmap' command.

        Args:
            output (str): The command output as a string.

        Returns:
            list of Client: Parsed client information with 'name' and 'ip' keys.
        """
        clients = []
        lines = output.splitlines()
        for line in lines:
            if 'Nmap scan report for' in line:
                parts = line.split()
                ip_address = parts[-1]
                host_name = parts[5].strip('()') if len(parts) == 5 else ""
                clients.append(Client(name=host_name, ip=ip_address))
        return clients

    def _resolve_hostname_to_ip(self, hostname):
        """
        Resolve a hostname to an IP address.

        Args:
            hostname (str): The hostname to resolve.

        Returns:
            str: The resolved IP address or an empty string if resolution fails.
        """
        try:
            return socket.gethostbyname(hostname)
        except socket.gaierror as e:
            logging.error(f"Failed to resolve hostname {hostname}: {e}")
            return ""