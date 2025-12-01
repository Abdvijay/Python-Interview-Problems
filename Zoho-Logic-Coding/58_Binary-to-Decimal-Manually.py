binary_value = input("Enter the binary value : ")
length = len(binary_value)
decimal_value = 0
for i in binary_value:
    decimal_value += int(i) * (2 ** (length-1))
    length -= 1
print(decimal_value)

# Sample Input and Sample Output :

# Enter the binary value : 1010
# 10

# Enter the binary value : 1011010
# 90