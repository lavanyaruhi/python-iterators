class RoutingTable:
    def __init__(self):
        self.entries = []

    def add_entry(self, destination, next_hop, metric):
        self.entries.append((destination, next_hop, metric))

    def __iter__(self):
        return RoutingTableIterator(self.entries)


class RoutingTableIterator:
    def __init__(self, entries):
        self.entries = entries
        self.index = 0

    def __next__(self):
        if self.index >= len(self.entries):
            raise StopIteration
        current_entry = self.entries[self.index]
        self.index += 1
        return current_entry


# Usage example: Traversing network routing table
routing_table = RoutingTable()
routing_table.add_entry("192.168.1.0/24", "192.168.1.1", 1)
routing_table.add_entry("10.0.0.0/8", "10.0.0.1", 2)
routing_table.add_entry("172.16.0.0/16", "172.16.0.1", 3)

for entry in routing_table:
    destination, next_hop, metric = entry
    print(f"Destination: {destination}, Next Hop: {next_hop}, Metric: {metric}")
