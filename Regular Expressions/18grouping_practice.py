import re

pattern = r'[\w](\w)[\d]([0-5])'

txt = "wa45 r4t3 2o51"

list = re.findall(pattern, txt)

print(list)