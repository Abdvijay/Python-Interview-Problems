# Input:
# Enter operation: +
# Enter numbers: 10 25

# Output:
# Result: 35

operation = input("Enter the operation to be performed : ")
a,b = map(int,input("Enter the a and b value : ").split())
if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    if b == 0:
        result = "Cannot divided by zero"
    else:
        result = a / b
elif operation == "//":
    if b == 0:
        result = "Cannot divided by zero"
    else:
        result = a // b
else:
    result = "Unsupported or Invalid operation :)"
if result.isdigit():
    print(f'The result of {a} {operation} {b} is {result}')
else:
    print(f'{result}')

# Enter the operation to be performed : +
# Enter the a and b value : 10 25
# The result of 10 + 25 is 35

# Enter the operation to be performed : // 
# Enter the a and b value : 9 0
# Cannot divided by zero

# Enter the operation to be performed : =
# Enter the a and b value : 2 5
# Unsupported or Invalid operation :)