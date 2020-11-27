items = ["c", "python", "java", "javascript", "html", "css"]

items2 = ["compiler", "interpreter", "debugger", "assembler"]

items3 = {"compiler", "interpreter", "debugger", "assembler"}

items4 = ("compiler", "interpreter", "debugger", "assembler")

items.extend(items2)

print(items)

items.extend(items3)

print(items)

items.extend(items4)

print(items)