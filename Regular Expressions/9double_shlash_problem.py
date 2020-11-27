import re

str = "python is \\interpreted"

print(str)

print(re.search(r"\\interpreted", str))