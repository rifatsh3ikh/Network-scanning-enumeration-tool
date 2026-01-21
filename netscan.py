import argparse
from colorama import Fore, init
from scanner.host_discovery import discover_hosts
from scanner.port_scanner import scan_ports
from scanner.service_enum import service_scan
from scanner.os_detection import detect_os

init(autoreset=True)

def banner():
    print(Fore.CYAN + """
 _   _      _   _____                 
| \ | |    | | / ____|                
|  \| | ___| |_| (___   ___ __ _ _ __ 
| . ` |/ _ \ __|\___ \ / __/ _` | '_ \\
| |\  |  __/ |_ ____) | (_| (_| | | | |
|_| \_|\___|\__|_____/ \___\__,_|_| |_|

 Network Scanner & Enumerator
    """)

def main():
    banner()

    parser = argparse.ArgumentParser(description="Network Scanning CLI Tool")
    parser.add_argument("target", help="Target IP or Network (e.g. 192.168.1.1 or 192.168.1.0/24)")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range (default 1-1024)")
    parser.add_argument("-s", "--service", action="store_true", help="Enable service enumeration")
    parser.add_argument("-o", "--os", action="store_true", help="Enable OS detection")

    args = parser.parse_args()

    print(Fore.YELLOW + "[*] Discovering live hosts...")
    hosts = discover_hosts(args.target)

    if not hosts:
        print(Fore.RED + "[-] No live hosts found")
        return

    for host in hosts:
        print(Fore.CYAN + f"\n[+] Host: {host}")
        ports = scan_ports(host, args.ports)

        if not ports:
            print("    No open ports")
            continue

        for port, state in ports.items():
            print(Fore.GREEN + f"    Port {port}: {state}")

        if args.service:
            service_scan(host, args.ports)
        if args.os:
            detect_os(host)


if __name__ == "__main__":
    main()
