from scrapli.driver.core import IOSXEDriver
from scrapli_inv import inv
from rich import print
from rich.pretty import Pretty, pprint
from rich.panel import Panel

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

    # Print raw ouput
    print(result.result)
    # Parse output using Genie templates
    genie_results = Pretty(result.genie_parse_output())
    genie_panel = Panel.fit(
        genie_results, title="[turquoise2]Genie Results[/turquoise2]"
    )
    print(genie_panel)

    # Parse output using TextFSM templates
    ntc_results = Pretty(result.textfsm_parse_output())
    ntc_panel = Panel.fit(ntc_results, title="[red]NTC Results[/red]")
    print(ntc_panel)

    # Parsing out the OS version
    device_version = result.genie_parse_output()
    print(f"[yellow]Device OS Version[/yellow]: {device_version['version']['version']}")


if __name__ == "__main__":
    main()
