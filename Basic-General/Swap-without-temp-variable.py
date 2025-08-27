# a = int(input("Enter the a value : "))
# b = int(input("Enter the b value : "))
# print("Before swaping : ", a, b)
# a, b = b, a
# print("After  swaping : ", a, b)

# Another method
a = int(input("Enter the a value : "))
b = int(input("Enter the b value : "))
print("Before swaping : ", a, b)
a = a + b
b = a - b
a = a - b
print("After  swaping : ", a, b)