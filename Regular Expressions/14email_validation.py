import re

email = "student@ail.com tuple@gmail.com doc@.com"

print("Emailmatches:",len(re.findall("[\w._%+-]{2,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email)))