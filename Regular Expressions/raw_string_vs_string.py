# In Python using slash before special character is deprecated
# solution this problem is using raw string
# r'\n' is different from "\n".
# r'\n' treated as two characters '\' and 'n' respectively.
# whereas "\n" is treated as new line character.
import re
pattern1 = r'\n'
pattern2 = "\n"
txt = "hello this\n is to de\nmonstrate re\ngular expressions\n"
print(re.findall(pattern1, txt))
print(re.findall(pattern2, txt))

