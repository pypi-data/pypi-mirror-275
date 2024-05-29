import unittest
from pynet_scanner import NetworkScanner

class TestNetworkScanner(unittest.TestCase):

    def test_discover_clients(self):
        scanner = NetworkScanner()
        clients = scanner.discover_clients()
        self.assertIsInstance(clients, list)
        for client in clients:
            self.assertIsInstance(client.name, str)
            self.assertIsInstance(client.ip, str)

if __name__ == '__main__':
    unittest.main()