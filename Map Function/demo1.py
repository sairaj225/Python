# python map function
"""
The map() function exicutes a specified 
function on items of an iterable. 
The item is sent to the function 
as parameter
"""

def power(a):
    return a * a

items = [1, 3, 4, 5, 6]

powers = map(power, items)

print(powers)

print(list(powers))