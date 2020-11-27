# We can use an "else" clause with a "for" loop in Python.
# It's a specail type of syntax that exicutes only if 
# the for loop exits naturally, without any break statement.

def func(array):
    for num in array:
        if num%2 == 0:
            print(num)
            break # CASE 1: Break is called, so 'else' wouldn't be exicuted.
    else: # CASE 2: 'else' exicuted since break is not called.
        print("No call for break. Else is exicuted")

print("1st case")
func([2])
print("2nd case")
func([3])