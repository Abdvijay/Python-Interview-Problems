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