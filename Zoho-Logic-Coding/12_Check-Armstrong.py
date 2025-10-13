# Sample Input
# Enter the number to check armstrong : 153

# Sample Output
# The given number 153 is armstrong number

number = int(input("Enter the number to check armstrong : "))
arms = 0
temp = number
while temp != 0:
    digit = temp % 10
    arms = arms + digit ** 3
    temp = temp // 10
if number == arms:
    print(f"The given number {number} is armstrong number")
else:
    print(f"The given number {number} is not an armstrong number")

# number = input("Enter the number to check armstrong : ")
# digits = [int(x) for x in number]
# arms = sum(map(lambda x: x ** 3,digits))
# if int(number) == arms:
#     print(f"The given number {number} is armstrong number")
# else:
#     print(f"The given number {number} is not an armstrong number")