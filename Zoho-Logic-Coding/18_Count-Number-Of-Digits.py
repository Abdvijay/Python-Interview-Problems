#Sample Input
# Enter the number : -238423

#Sample Output
# The number of digits in a number -238423 is 6

number = int(input("Enter the number : "))
count = 0
if number == 0:
    count = 1
else:
    temp = abs(number) # Handle negative number
    while temp > 0:
        temp //= 10
        count += 1
print(f"The number of digits in a number {number} is {count}")