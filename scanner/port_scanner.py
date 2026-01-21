import nmap

def scan_ports(host, ports):
    nm = nmap.PortScanner()
    nm.scan(hosts=host, ports=ports, arguments="-sT")

    open_ports = {}

    if host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto]:
                state = nm[host][proto][port]["state"]
                if state == "open":
                    open_ports[port] = state

    return open_ports
