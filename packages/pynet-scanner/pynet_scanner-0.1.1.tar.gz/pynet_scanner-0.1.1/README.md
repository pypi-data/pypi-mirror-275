# Network Scanner

Network Scanner is a Python package for discovering clients in your local network. It provides a simple interface to scan for devices and retrieve information such as hostname and IP address.

## Installation

You can install the package via pip:

```bash
pip install pynet_scanner
```

## Usage

```
from pynet_scanner import NetworkScanner

# Create a NetworkScanner instance
scanner = NetworkScanner()

# Discover clients in the local network
clients = scanner.discover_clients()

# Print information about each discovered client
for client in clients:
    print(client)
```

## Features

- Scan for clients in the local network using `NetworkScanner` class.
- Supports both Windows and Linux platforms.
- Retrieves hostname and IP address for each discovered client.

## Dependencies
The package relies on the following dependencies:

- `nmap`: Used for network scanning on Linux platforms.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.