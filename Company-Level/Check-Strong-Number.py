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