import re

Nameage = '''
Sai is 22 and Raje is 22
and Sairaje is 2
'''
ages = re.findall(r'\d{1,3}', Nameage)
names = re.findall(r'[A-Z][a-z]*', Nameage)

ageDict = {}
x = 0

for eachname in names:
    ageDict[eachname] = ages[x]
    x+=1

print(ageDict)

