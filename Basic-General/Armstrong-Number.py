number = int(input("Enter the number : "))
temp = number
sum = 0
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10
if number == sum:
    print(f'The given number {number} is Armstrong number')
else:
    print(f'The given number {number} is not an Armstrong number')