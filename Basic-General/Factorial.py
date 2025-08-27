def fact(num):
    result = 1
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        for i in range(1,num+1):
            result *= i
        return result
number = int(input("Enter the number to find a factorial : "))
result = fact(number)
print(f'The factorial of {number} is : {result}')