d = {
    "name" : 'sairaju',
    "roll no" : 225,
    "class" : "MCA"
}

d.update({"grade" : "A"})
d.update({"name" : "sairaje"})

print(d)

# setdefault() method insets and also returns the value of item with specified key
x=d.setdefault('blood group', "B+")
print(d)
print(x)

x=d.setdefault('grade', "A+")
print(d)
print(x)