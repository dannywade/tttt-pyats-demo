from scrapli.driver.core import IOSXEDriver
from pprint import pprint
from scrapli_inv import inv

"""
Script that uses Scrapli to connect and collect data from the device(s), and uses
Genie to parse it.
"""

dev = inv.get("router-1")


MY_DEVICE = {
    "host": dev.get("host"),
    "auth_username": dev.get("user"),
    "auth_password": dev.get("pass"),
    "auth_secondary": dev.get("enable_pass"),  # Enable password (if used)
    "auth_strict_key": False,
    "ssh_config_file": "config",  # Need to include for older cipher suites (vIOS 15.x)
}


def main():
    """Simple example demonstrating how to parse structured data via Genie parsers"""
    with IOSXEDriver(**MY_DEVICE) as conn:
        # Platform drivers will auto-magically handle disabling paging for you
        result = conn.send_command("show version")

    print(result.result)
    pprint(result.genie_parse_output())

    # Parsing out the OS version
    # device_version = result.genie_parse_output()
    # print(device_version["version"]["os"])


if __name__ == "__main__":
    main()
