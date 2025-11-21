number = int(input("Enter the decimal value : "))
temp = number
binary = []
while True:
    if number != 1:
        quotient = number // 2
        remainder = number % 2
        number = number // 2
        binary.append(str(remainder))
    else:
        binary.append(str(number))
        result = binary[::-1]
        print(f"The binary value of {temp} is {''.join(result)}")
        break

# Sample Input and Sample Output

# Enter the decimal value : 10
# The binary value of 10 is 1010

# Enter the decimal value : 1
# The binary value of 1 is 1