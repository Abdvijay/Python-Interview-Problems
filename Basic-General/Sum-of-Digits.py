# Enter the number : 102
# The sum of 102 is 3

number = input("Enter the number : ")
sum = 0
for i in number:
    sum += int(i)
print(f'The sum of {number} is {sum}')