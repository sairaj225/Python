d = {
    "name" : 'sairaju',
    "roll no" : 225
}

print(d)
# Accessing the dictionary
print(d['roll no'])
print(d.get('name'))

# Changing the value of the dictionary key
d['name'] = "raje"
print(d)

# Adding new item into dictionary
d["class"] = "MCA"
print(d)

# Dictionary length
print(len(d))