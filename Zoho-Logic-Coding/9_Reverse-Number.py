# Sample Input
# Enter the number to print in reverse order : 1234

# Sample Output
# The revere number of 1234 is 4321

number = int(input("Enter the number to print in reverse order : "))
temp = number
rev = 0
while temp != 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
print(f"The revere number of {number} is {rev}")