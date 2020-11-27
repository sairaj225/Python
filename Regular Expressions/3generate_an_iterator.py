import re

# finditer() returns starting as well as the ending index of a word
# in the given string

str = "we have said hello to him, and he replied with hellora hello"

for i in re.finditer("hello", str):

    lockup = i.span()

    print(lockup)