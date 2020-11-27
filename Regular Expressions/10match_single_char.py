import re

randStr = "12345"
print("Matches:",len(re.findall("\d{5}", randStr)))

print("Matches:",len(re.findall("\d", randStr)))

print("Matches:",len(re.findall("\D", randStr)))

number_series = "1 12 123 1234 12345 123456 1234567"

print("Matches:",len(re.findall("\d{4,6}", number_series)))