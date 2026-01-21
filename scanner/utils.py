from colorama import Fore

RISK_LEVELS = {
    "ftp": ("🔴 HIGH", Fore.RED),
    "ssh": ("🔴 HIGH", Fore.RED),
    "telnet": ("🔴 HIGH", Fore.RED),
    "mysql": ("🔴 HIGH", Fore.RED),
    "mongodb": ("🔴 HIGH", Fore.RED),
    "http": ("🟡 MEDIUM", Fore.YELLOW),
    "https": ("🟢 LOW", Fore.GREEN),
}


def get_risk(service_name):
    service_name = service_name.lower()

    for key in RISK_LEVELS:
        if key in service_name:
            return RISK_LEVELS[key]

    return ("MEDIUM", Fore.YELLOW)
