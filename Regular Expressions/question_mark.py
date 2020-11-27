import re

pattern = r'ab?cd'

txt = "bcd abcd acd"

list = re.findall(pattern, txt)

print(list)