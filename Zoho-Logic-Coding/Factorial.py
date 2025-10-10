# Sample Input
# Enter the number to find factorial : 5

# Sample Output
# The factorial of 5 is 120

number = int(input("Enter the number to find factorial : "))
fact = 1
for i in range(1,number+1):
    fact = fact * i
print(f"The factorial of {number} is {fact}")