number = int(input("Enter the number to find factorial : "))
result = 1
if number == 0:
    print(f'Factorial of {number} is 1')
elif number == 1:
    print(f'Factorial of {number} is 1')
else:
    for i in range(number,0,-1):
        result = result * i
    print(f'Factorial of {number} is {result}')

# OUTPUT

# Enter the number to find factorial : 0
# Factorial of 5 is 120

# Enter the number to find factorial : 0
# Factorial of 0 is 1

# Enter the number to find factorial : 1
# Factorial of 1 is 1

# Enter the number to find factorial : 4
# Factorial of 4 is 24