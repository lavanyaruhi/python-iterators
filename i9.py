import netifaces as ni
import pyroute2

# Get the default interface
default_interface = ni.gateways()['default'][ni.AF_INET][1]

# Create a netlink socket
ip = pyroute2.IPDB()

# Get the routing table for the default interface
routing_table = ip.routes.tables[default_interface]

# Create an iterator over the routing table
routing_table_iterator = iter(routing_table)

# Traverse the routing table using the iterator
for route in routing_table_iterator:
    print(route)
