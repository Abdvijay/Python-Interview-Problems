# Check Strong Number

# (A number is strong if sum of factorial of digits = number)

# Input: 145 → 1!+4!+5!=145

# Output: Strong Number

# Input: 123

# Output: Not Strong Number

number = int(input("Enter the number : "))
total = 0
temp = number
def fact(num):
    sum = 1
    for i in range(1,num+1):
        sum *= i 
    return sum
while number != 0:
    total += fact(number % 10)
    number = number // 10
print(total)
if temp == total:
    print(f'The given number {temp} is Strong Number')
else:
    print(f'The given number {temp} is not an Strong Number')