# The zip() function returns a zip object, 
# which is an iterator of tuples where 
# the first item in each passed iterator is paired together, 
# and then the second item in each passed iterator are paired together etc.

l1 = [1, 3, 5, 6]
l2 = ['a', 'b', 'c', 't']
z = zip(l1,l2)
print(list(z))

# If the passed iterators have different lengths, 
# the iterator with the least items decides 
# the length of the new iterator.

l3 = ["apple", "banana", "grapes"]
z2 = zip(l1, l2, l3)
print(list(z2))