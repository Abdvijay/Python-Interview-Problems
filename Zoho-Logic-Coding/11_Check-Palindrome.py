# Sample input
# Enter the number to check palindrome : 121 

# Sample Output
# The number 121 is palindrome

# number = int(input("Enter the number to check palindrome : "))
# temp = number
# rev = 0
# while temp != 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp //= 10
# if number == rev :
#     print(f"The number {number} is palindrome")
# else:
#     print(f"The number {number} is not palindrome")

number = input("Enter the number to check palindrome : ")
if number == number[::-1]:
    print(f"The number {number} is palindrome")
else:
    print(f"The number {number} is not palindrome")