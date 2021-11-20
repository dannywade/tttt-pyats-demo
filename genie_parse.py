import os
from pyats.topology.loader import load
from pprint import pprint

"""
Script used to load a pyATS testbed file (testbed.yaml), connect to a device (router-1),
and parse 'show version' using the Genie library
"""

testbed_file = os.path.join(os.path.dirname(__file__), "testbed.yaml")

testbed = load(testbed_file)

r1 = testbed.devices["router-1"]

r1.connect()
if r1.connected():  # returns True/False
    print("Connected to Router 1!")
else:
    print("Could not connect to specified device!")

# Collect and parse 'show version' command from Router 1 device
show_ver_raw = r1.execute("show version")  # returns a string value - unstructured
pprint(show_ver_raw)

show_ver_struct = r1.parse("show version")  # returns a dictionary - structured
pprint(show_ver_struct)

r1.disconnect()
