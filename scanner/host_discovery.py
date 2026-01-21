import nmap

def discover_hosts(target):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments="-sn")

    live_hosts = []
    for host in nm.all_hosts():
        if nm[host].state() == "up":
            live_hosts.append(host)

    return live_hosts
