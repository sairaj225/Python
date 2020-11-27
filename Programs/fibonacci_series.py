def fibonacci(n):
    number1=0
    number2=1
    for i in range(n):
        print(number1, end=" ")
        next_numer=number1+number2
        number1=number2
        number2=next_numer
fibonacci(7)