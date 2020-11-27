import re

# \w = [a-zA-Z0-9_]
# \W = [^a-zA-Z0-9_]

phone_number = "412-555-1212"

if re.search("\w{3}-\w{3}-\w{4}", phone_number):
    print("It is a phone number")


if re.search("\d{3}-\d{3}-\d{4}", phone_number):
    print("It is a phone number")