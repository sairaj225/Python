thislist = ["apple", "banana", "cherry"]

newlist1 = thislist.copy()

print(newlist1)

newlist2 = list(thislist)

print(newlist2)

newlist3 = thislist

thislist.pop()

print(newlist3)