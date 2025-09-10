# Enter the first number : 4
# Enter the second number : 5
# Enter the third number : 6
# 6 is the Largest number


a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
if a > b and a > c:
    print(f'{a} is the Largest number')
elif b > a and b > c:
    print(f'{b} is the Largest number')
else:
    print(f'{c} is the Largest number')