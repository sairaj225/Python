string = input("Enter a string: ")
reverse_string = string[::-1]
print("Palindrome") if string == reverse_string else print("Not Palindrome")