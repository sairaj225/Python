import math
def prime(n):
    for i in range(2,math.ceil(n/2)):
        if n%i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
    
prime(36)