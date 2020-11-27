# TODO: Syntax: max(iterable, *iterables, key, default)
# iterable - an iterable such as list, tuple, set, dictionary, etc.
# *iterables (optional) - any number of iterables; can be more than one.
'''
key (optional) - key function where the iterables are passed and comparison is 
performed based on its return value.
'''
# default (optional) - default value if the given iterable is empty.

l = [1, 3, 5, 7, 9]
max_element = max(l)
print(max_element)

l2=[]
max_element = max(l2, default="Empty Iterable")
print(max_element)

l3 = [1, -2, -9, -3]
l4 = [-2, 5, 6, 7]
max_element = max(l4, l3)
print(max_element)

l5 = [1, 3, 5, 6, 7, 7, 8, 6, 8, 9, 4, 2, 4, 4]
print(max(l5)) 
print( max( l5, key = lambda a: a * (-a) ))
