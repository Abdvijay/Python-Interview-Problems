# Sample input
# Enter the number to find sum of digits : 1234

# Sample Output
# The sum of digits of number 1234 is 10

number = int(input("Enter the number to find sum of digits : "))
total = 0
temp = number
while temp != 0:
    digit = temp % 10
    total = total + digit
    temp = temp // 10
print(f"The sum of digits of number {number} is {total}")