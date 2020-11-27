from random import randint 

password = ''

for n in range(15): # 15 Characters
    password = password + chr( randint( 33, 127 ) ) # 33-127 ASCII code positions

print(password)