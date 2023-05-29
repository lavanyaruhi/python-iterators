import configparser

class NetworkConfig:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def __iter__(self):
        return NetworkIterator(self.config)


class NetworkIterator:
    def __init__(self, config):
        self.sections = config.sections()
        self.current_section = 0

    def __next__(self):
        if self.current_section >= len(self.sections):
            raise StopIteration

        section = self.sections[self.current_section]
        options = self.config[section]
        self.current_section += 1

        return section, options


# Usage example: Parsing network configuration file
network_config = NetworkConfig("network.ini")

for section, options in network_config:
    print("Section:", section)
    for option in options:
        value = options[option]
        print(f"{option}: {value}")
    print()
