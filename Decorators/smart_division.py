def smart_division(func):
    def inner(a, b):
        if b==0:
            print("We cann't divide")
            return
        return func(a, b)
    return inner

@smart_division
def divide(a, b):
    return a/b

print(divide(2, 9))
print(divide(2, 0))

