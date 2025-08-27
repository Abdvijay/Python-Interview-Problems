# (Sum of digits until single digit is 1 → then Magic Number)

# Input: 19 → 1+9=10 → 1+0=1

# Output: Magic Number

# Input: 123 → 1+2+3=6

# Output: Not Magic Number

number = int(input("Enter the number to check magic number or not : "))
temp = number

# Keep summing digits until single digit
while number >= 10:   # repeat until number becomes single digit
    s = 0
    while number > 0:
        s += number % 10
        number //= 10
    number = s   # replace with sum of digits

# Final check
if number == 1:
    print(f"The number {temp} is a Magic Number")
else:
    print(f"The number {temp} is Not a Magic Number")