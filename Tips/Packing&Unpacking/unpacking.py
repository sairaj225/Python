'''
1. The process of splitting the packed values into individual elements is called ‘unpacking’.
2. The packed values are strings, lists, tuples, sets, and dictionaries.
3. During the unpacking elements from RHS (Right Hand Side) are split into 
its relative position on the LHS (Left Hand Side). 
We will see how this works in the following examples.
'''

x, y, z, l = "Java"
print(x,y,z,l)

a, b, c = [1, 2, 3]
print(a,b,c)

a, b, c = (1, 2, 3)
print(a,b,c)

a, b, c = {1:1, 2:4, 3:9}
print(a,b,c)

# Extended iterable UNPACKING
# The extended iterable unpacking is done via the operators * and **

x, *y, z = "Java"
print(x,y,z)

*a, b, c = [1, 2, 3, 4, 5]
print(a,b,c)

a, *b, c = {10, 20, 30, 40}
print(a, b, c)

a, b, *c = (1, 2, 3, 4, 5)
print(a,b,c)

a, *b, c = {1:1, 2:4, 3:9, 4:16, 5:25}
print(a,b,c)

# ** Operator
# As you have noticed from the above examples, 
# * operator iterates through the keys in the dictionary. 
# If we would like to iterate through key-value pairs, then we must use ** operator.

a, *b, c = {1:1, 2:4, 3:9, 4:16, 5:25}
print(a,b,c)

d1 = {1:1, 2:4, 3:9, 4:16, 5:25}
d2 = {6:36, 7:49, 8:64, 9:81}

# d3 = {d1, d2}
# print(d3)

d4 = {*d1, *d2}
print(d4)

d5 = {**d1, **d2}
print(d5)

# Nested UPACKING
a, *b , (c, *d, e) = [1, 3, 5, (1, 3, 5, 7, 8)]
print(a, b, c, d, e)