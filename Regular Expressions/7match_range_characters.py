import re

str = "Sat, hat, mat, pat, lat"

match_words = re.findall("[h-m]at", str)

for i in match_words:
    print(i)

print("**********************")
match_words = re.findall("[^h-m]at", str)

for i in match_words:
    print(i)