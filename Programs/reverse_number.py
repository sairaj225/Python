import sys

n = int(sys.argv[1])

sign = 1 if n > 0 else -1
str_number = str(abs(n))
str_number = str_number[::-1]

r = sign * int(str_number)
print(r)