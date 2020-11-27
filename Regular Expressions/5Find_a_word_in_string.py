import re


# if re.search("hello", "we have said hello to him, and he replied with hellora hello"):
#     print("There is hello in the string")

# findall() returns list of all matches
words = re.findall("hello", "we have said hello to him, and he replied with hellora hello")
for i in words:
    print(i)
