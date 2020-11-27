import re

str = '''
I haven't had my dinner
I'm peckish
I want something to eat
'''
print(str)

regEx = re.compile("\n")
str = regEx.sub(" ", str)

print(str)