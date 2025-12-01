def find_HCF(a,b):
    if b == 0:
        return a
    return find_HCF(b,a % b)

def find_LCM(a,b):
    return (a * b) //  find_HCF(a,b)


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print(f"HCF of {num1} and {num2} is {find_HCF(num1, num2)}")
print(f"LCM of {num1} and {num2} is {find_LCM(num1, num2)}")


# Sample Input and Sample Output :

# Enter first number : 56
# Enter second number : 34
# HCF of 56 and 34 is 2
# LCM of 56 and 34 is 952