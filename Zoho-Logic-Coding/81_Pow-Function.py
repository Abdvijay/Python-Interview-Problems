x = int(input("Enter the base value : "))
n = int(input("Enter the pow value : "))
if n == 0:
    result = 1
else:
    result = x ** n
print(f"Pow({x},{n}) is {result}")

# Sample Input and Sample Output

# Enter the base value : 3
# Enter the pow value : 3
# Pow(3,3) is 27

# Enter the base value : 2
# Enter the pow value : 5
# Pow(2,5) is 32

# Enter the base value : 4
# Enter the pow value : 0
# Pow(4,0) is 1