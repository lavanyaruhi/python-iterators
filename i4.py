class Route:
    def __init__(self, destination, next_hop, metric):
        self.destination = destination
        self.next_hop = next_hop
        self.metric = metric

class RoutingTable:
    def __init__(self):
        self.routes = []

    def add_route(self, destination, next_hop, metric):
        route = Route(destination, next_hop, metric)
        self.routes.append(route)

    def __iter__(self):
        return iter(self.routes)

# Example usage: Traversing a routing table
routing_table = RoutingTable()
routing_table.add_route("192.168.0.0/24", "192.168.1.1", 1)
routing_table.add_route("10.0.0.0/8", "10.1.1.1", 2)
routing_table.add_route("172.16.0.0/16", "172.16.1.1", 3)

for route in routing_table:
    print("Destination:", route.destination)
    print("Next Hop:", route.next_hop)
    print("Metric:", route.metric)
    print("-------------")
