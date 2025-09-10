# Enter the number to check prime or not : 10
# Number 10 is Not a Prime-Number

number = int(input("Enter the number to check prime or not : "))
flag = True
for i in range(2,number):
    if number < 3:
        flag = True
    if number % i == 0:
        flag = False
        break
if flag:
    print(f'Number {number} is Prime-Number')
else:
    print(f'Number {number} is Not a Prime-Number')