import nmap
from colorama import Fore
from scanner.utils import get_risk

def service_scan(host, ports):
    print(Fore.MAGENTA + "\n    [*] Service Enumeration & Risk Analysis")

    nm = nmap.PortScanner()
    nm.scan(hosts=host, ports=ports, arguments="-sV")

    if host not in nm.all_hosts():
        return

    for proto in nm[host].all_protocols():
        for port in nm[host][proto]:
            svc = nm[host][proto][port]

            name = svc.get("name", "unknown")
            product = svc.get("product", "")
            version = svc.get("version", "")

            banner = f"{name} {product} {version}".strip()

            risk, color = get_risk(name)

            print(
                color
                + f"    Port {port:<5} | {banner:<30} | {risk}"
            )
