# Network Scanning & Enumeration Tool

## ⚠️ Legal Disclaimer

This tool is intended for educational and authorized security testing purposes only. You are responsible for ensuring you have explicit permission to scan the target systems. Unauthorized scanning of networks or systems you do not own or have permission to test may be illegal. The author is not responsible for misuse of this tool.

## Overview

A command-line tool built with Python for network scanning and enumeration. This utility leverages the power of `nmap` to provide host discovery, port scanning, service enumeration, and OS detection capabilities.

## Features

*   **Host Discovery:** Identifies live hosts on a network using ping scans.
*   **Port Scanning:** Scans for open TCP ports on target hosts.
*   **Service Enumeration:** Identifies services running on open ports, including their versions.
*   **OS Detection:** Attempts to identify the operating system of the target host.
*   **Risk Analysis:** Provides a basic risk level (High, Medium, Low) for common services.
*   **Colorized Output:** Uses `colorama` for a more readable and organized command-line output.

## Prerequisites

This tool is a wrapper around the `nmap` command-line utility. You must have `nmap` installed on your system for this script to function correctly.

*   **On Debian/Ubuntu:** `sudo apt-get install nmap`
*   **On CentOS/RHEL:** `sudo yum install nmap`
*   **On macOS (with Homebrew):** `brew install nmap`

## Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/rifatsh3ikh/network-scanning-enumeration-tool.git
    cd network-scanning-enumeration-tool
    ```

2.  **Install Python dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

The main script is `netscan.py`. All scans are initiated from this file.

```sh
python netscan.py <target> [options]
```

**Arguments:**

| Argument          | Description                                                    | Default  |
| ----------------- | -------------------------------------------------------------- | -------- |
| `target`          | Target IP or network (e.g., `192.168.1.1` or `192.168.1.0/24`)  | Required |
| `-p`, `--ports`   | Port range to scan                                             | `1-1024` |
| `-s`, `--service` | Enable service enumeration and risk analysis                   | `False`  |
| `-o`, `--os`      | Enable OS detection (requires root/administrator privileges)   | `False`  |

**Examples:**

**Basic Host Discovery and Port Scan (Ports 1-1024)**

```sh
python netscan.py 192.168.1.1
```

**Scan a Specific Port Range on a Network**

```sh
python netscan.py 192.168.1.0/24 -p 22,80,443
```

**Perform Service Enumeration**

```sh
python netscan.py 192.168.1.10 -s
```

**Perform OS Detection (Requires sudo/admin)**

```sh
sudo python netscan.py 192.168.1.10 -o
```

**Full Scan (Ports, Services, and OS)**

```sh
sudo python netscan.py 192.168.1.10 -p 1-65535 -s -o
```

## 🤝 Contributing

Contributions are welcome!
To contribute:

Fork the project

Create a feature branch (git checkout -b feature/your‑idea)

Commit your changes (git commit -m "Add feature")

Push to your branch (git push)

Open a Pull Request

## 📬 Contact

Maintained by rifatsh3ikh

## License

This project is licensed under the MIT License. See the [License](License) file for details.
