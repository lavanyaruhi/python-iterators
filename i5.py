class PacketCapture:
    def __init__(self):
        self.packets = []

    def add_packet(self, packet):
        self.packets.append(packet)

    def __iter__(self):
        return PacketIterator(self.packets)


class PacketIterator:
    def __init__(self, packets):
        self.packets = packets
        self.index = 0

    def __next__(self):
        if self.index >= len(self.packets):
            raise StopIteration
        current_packet = self.packets[self.index]
        self.index += 1
        return current_packet


# Usage example: Enumerating network packets
packet_capture = PacketCapture()
packet_capture.add_packet("Packet 1")
packet_capture.add_packet("Packet 2")
packet_capture.add_packet("Packet 3")

for packet in packet_capture:
    print(packet)
