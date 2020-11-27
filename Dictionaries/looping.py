d = {
    "name" : 'sairaju',
    "roll no" : 225,
    "class" : "MCA"
}

# looping through dictionary
for x in d:
    print(x, end=" ")

for x in d:
    print(d[x], end=" ")

for x in d.values():
    print(x, end=" ")

for x, y in d.items():
    print("{} : {}".format(x, y))