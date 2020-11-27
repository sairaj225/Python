fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newitems = [x for x in fruits if "a" in x]

print(newitems)

newitems = [x.upper() for x in fruits]

print(newitems)