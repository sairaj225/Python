items1 = ["apple", "banana", "grapes", "oranges"]
items2 = ["simla", "ap", "kerala", "ap"]

def add_items(a, b):
    return a +" - "+ b

final_items = map(add_items, items1, items2)

print(final_items)

print(list(final_items))