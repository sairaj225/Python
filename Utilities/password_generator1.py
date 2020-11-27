import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%&*'
digits = '0123456789'

all = lower + upper + symbols + digits

length = 8

password = "".join(random.sample(all, length))

print(password)