def fact(num):
    if num == 1:
        return 1
    elif num == 0:
        return 1
    else:
        return num * fact(num-1)
number = int(input("Enter the number to find a factorial : "))
result = fact(number)
print(f'The factorial of {number} is {result}')