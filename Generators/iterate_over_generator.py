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
    
# We can use for loop with generators 
for item in first_generator():
    print(item)