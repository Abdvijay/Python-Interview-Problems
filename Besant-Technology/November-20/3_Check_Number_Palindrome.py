number = input("Enter the number : ")
if number == number[::-1]:
    print(f'The given number {number} is Palindrome')
else:
    print(f"The given number {number} is not a Palindrome")

# Without Build in function

# number = int(input("Enter the number : "))
# temp = number
# result = 0
# while temp > 0:
#     digit = temp % 10
#     result = result * 10 +  digit
#     temp = temp // 10
# if result == number:
#      print(f'The given number {number} is Palindrome')
# else:
#     print(f"The given number {number} is not a Palindrome")


# OUTPUT

# Enter the number : 1234
# The given number 1234 is not a Palindrome

# Enter the number : 12121
# The given number 12121 is Palindrome