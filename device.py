from pyats.topology import Device, Testbed, Interface
from rich import inspect

# Documentation: https://developer.cisco.com/docs/pyats/api/: Testbed & Topology Info -> Everything is an Object

# Create and inspect Device object
device1 = Device("router1")
inspect(device1, methods=True)

# Create and inspect Interface object
interface1 = Interface("Eth1/1", "ethernet")  # breakpoint
inspect(interface1, methods=True)

# Add IPv4 address to Interface object
interface1.ipv4 = "10.1.1.1"  # breakpoint
inspect(interface1)

# Add Interface to Device
device1.add_interface(interface1)  # breakpoint
inspect(device1)

# Create and inspect Testbed object
testbed_a = Testbed(name="firstTestbed", alias="myTestbed")  # breakpoint
inspect(testbed_a, methods=True)

# Add Device to Testbed
testbed_a.add_device(device1)  # breakpoint
inspect(testbed_a)
