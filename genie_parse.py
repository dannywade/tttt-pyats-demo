import os
from pyats.topology.loader import load
from rich import print
from rich.pretty import Pretty
from rich.panel import Panel

"""
Script used to load a pyATS testbed file (testbed.yaml), connect to a device (router-1),
and parse 'show version' using the Genie library
"""
from dotenv import load_dotenv

# Load env vars found in .env file
load_dotenv()

eve_user = os.environ["EVE_USER"]
eve_pass = os.environ["EVE_PASS"]

testbed_file = os.path.join(os.path.dirname(__file__), "testbed.yaml")

testbed = load(testbed_file)

r1 = testbed.devices["router-1"]

r1.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)
# if r1.connected():  # returns True/False
#     print("Connected to Router 1!")
# else:
#     print("Could not connect to specified device!")


# Collect and parse 'show version' command from Router 1 device
show_ver_raw = Pretty(
    r1.execute("show version")
)  # returns a string value - unstructured
raw_panel = Panel.fit(show_ver_raw, title="[red]Unstructured Output[/red]")
print(raw_panel)

show_ver_struct = Pretty(r1.parse("show version"))  # returns a dictionary - structured
struct_panel = Panel.fit(
    show_ver_struct, title="[turquoise2]Structured Output[/turquoise2]"
)
print(struct_panel)

r1.disconnect()
