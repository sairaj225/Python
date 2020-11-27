'''
Generators are used to create iterators, 
but with a different approach. 
Generators are simple functions which return an iterable set of items, 
one at a time, in a special way.
'''
# If a function contains at least one yield statement
# It becames a Generator function.
# Generator function contains one or more yield statements.
'''
both 'yeild' and 'return' returns the same value.
'''
# when the function terminates, StopIteration is raised automatically on further calls.

# A simple generator function.
def first_generator():
    n=1
    print("First statement")
    yield n

    n=n+1
    print("Second statement")
    yield n

    n=n+1
    print("Third statement")
    yield n

a = first_generator()

print(next(a))
print(next(a))
print(next(a))
print(next(a))