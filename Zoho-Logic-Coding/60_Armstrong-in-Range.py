start = int(input("Enter the start value : "))
end = int(input("Enter the end value : "))
print(f"Armstrong numbers between {start} and {end} are : ", end="")
for i in range(start,end+1):
    result = 0
    temp = i
    power = len(str(i))
    while temp > 0:
        digit = temp % 10
        result = result + digit ** power
        temp = temp // 10
    if i == result:
        print(result,end=" ")

# Sample Input and Sample Output :

# Enter the start value : 1
# Enter the end value : 500
# Armstrong numbers between 1 and 500 are : 1 2 3 4 5 6 7 8 9 153 370 371 407 