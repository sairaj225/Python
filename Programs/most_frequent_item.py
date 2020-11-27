test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4] 

item = max(set(test), key = test.count)

print(item)