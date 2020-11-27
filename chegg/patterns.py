
import random
def create_code():
    digits = '0123456789'*2
    length = 20
    code = "".join(random.sample(digits, length))
    return code

def create_link():
    work_type = input("What kind of work you are submitting: ")
    lecture_code = input("What lecture are you posting this work for: ")
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    KU_id = input("What is your KU ID: ")
    number = random.randint(15,40)
    upper = 'ABCDEFGHIJLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    letters = upper+lower+digits
    code = "".join(random.sample(letters, number))
    return f'https://ku.blackboard.com/{work_type}/{lecture_code}/{name[0]}.{surname}.{name[-1]}-{KU_id[-3:]}/{code}'

def main():
    code = create_code()
    link = create_link()
    print("Your code is: ", code)
    print("Your link is: ", link)

main()







