# Bubble Sort Algorithm

items = []
number_of_items = int(input("Enter number of elements: "))
for i in range(number_of_items):
    item = int(input("Enter item: "))
    items.append(item)
for i in range(number_of_items-1):
    for j in range(number_of_items-1-i):
        if items[j]>items[j+1]:
            items[j], items[j+1] = items[j+1], items[j]

print(items)
