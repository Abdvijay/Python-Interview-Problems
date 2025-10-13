# Sample Input
# Enter the number to check prime or not : 14

# Sample Output
# The given number 14 is Not a Prime Number

number = int(input("Enter the number to check prime or not : "))
flag = True
for i in range(2,number):
    if number % i == 0:
        flag = False
        break
if flag:
    print(f"The given number {number} is Prime Number")
else:
    print(f"The given number {number} is Not a Prime Number")