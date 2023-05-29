class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        current_element = self.data[self.index]
        self.index += 1
        return current_element

# Example usage: Iterating over a list using custom iterator
my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_list)

for element in my_iterator:
    print(element)
