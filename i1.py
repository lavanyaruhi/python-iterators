my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

#print(next(my_iterator))  # Output: 1
#print(next(my_iterator))  # Output: 2
#print(next(my_iterator))  # Output: 3
#print(next(my_iterator))  # Output: 4
#print(next(my_iterator))  # Output: 5

# Using a for loop
#for element in my_iterator:
    #print(element)  # Output: Nothing will be printed because the iterator is already exhausted
 #   pass
# Using the next() function
#my_iterator = iter(my_list)
while True:
    try:
        element = next(my_iterator)
        print(element)
    except StopIteration:
        break
