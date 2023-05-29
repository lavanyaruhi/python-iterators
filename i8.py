class NetworkConfigParser:
    def __init__(self, config_file):
        self.config_file = config_file

    def parse(self):
        with open(self.config_file, 'r') as file:
            for line in file:
                yield self.process_line(line.strip())

    def process_line(self, line):
        # Logic to extract relevant information from the line
        # For the sake of simplicity, let's assume we're interested in lines starting with "interface"
        if line.startswith("interface"):
            return line

# Usage example: Parsing network configuration file
config_parser = NetworkConfigParser("network.conf")

for entry in config_parser.parse():
    print(entry)
