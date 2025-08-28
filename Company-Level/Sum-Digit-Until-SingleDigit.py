# Sum of Digits Until Single Digit

# Input: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2

# Output: 2

number = int(input("Enter the number : "))
temp = number
while number >= 10:
    result = 0
    while number > 0:
        digit = number % 10
        result += digit
        number = number // 10
    number = result
print(f'Number is {temp} -> {result}')