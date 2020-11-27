import re
str = "Sat, hat, mat, pat"

all_str = re.findall("[shmp]at", str)

for i in all_str:
    print(i)