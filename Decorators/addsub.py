def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def operation(func, a, b):
    result = func(a, b)
    print(result)
operation(add, 2, 4)
operation(sub, 4, 5)