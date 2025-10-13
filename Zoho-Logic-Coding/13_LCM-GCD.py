# Sample input
# Enter the a value : 12
# Enter the b value : 15

# Sample Output
# GCD of 12 and 15 is 3
# LCM of 12 and 15 is 60

a = int(input("Enter the a value : "))
b = int(input("Enter the b value : "))

def GCD(a,b):
    while b:
        a, b = b, a % b
    return a

def LCM(a,b):
    return (a * b) // GCD(a,b)

print(f"GCD of {a} and {b} is {GCD(a,b)}")
print(f"LCM of {a} and {b} is {LCM(a,b)}")