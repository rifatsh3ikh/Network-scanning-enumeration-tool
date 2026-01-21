import nmap
from colorama import Fore

def detect_os(host):
    print(Fore.BLUE + "    [*] OS Detection")

    nm = nmap.PortScanner()

    try:
        nm.scan(hosts=host, arguments="-O")
    except nmap.PortScannerError:
        print(Fore.RED + "    OS detection requires elevated privileges")
        return

    if host not in nm.all_hosts():
        print("    OS detection failed")
        return

    os_matches = nm[host].get("osmatch", [])

    if not os_matches:
        print("    OS could not be reliably detected")
        return

    best_match = os_matches[0]

    os_name = best_match.get("name", "Unknown")
    accuracy = best_match.get("accuracy", "N/A")

    print(Fore.BLUE + f"    OS Detected : {os_name}")
    print(Fore.BLUE + f"    Accuracy    : {accuracy}%")

    if "osclass" in best_match and best_match["osclass"]:
        device_type = best_match["osclass"][0].get("type", "Unknown")
        print(Fore.BLUE + f"    Device Type : {device_type}")
