#function

def addNumber(n):
    return lambda a: a+n

duble = addNumber(2)
triple = duble(4)

print(triple)