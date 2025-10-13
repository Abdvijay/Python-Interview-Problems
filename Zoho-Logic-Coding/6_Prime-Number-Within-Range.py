# Sample Input
# Enter the range : 10 45

# Sample Output
# Prime numbers between 10 to 45 is [11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

start,end = list(map(int,input("Enter the range : ").split()))
result = []
for i in range(start,end+1):
    flag = True
    for j in range(2,i):
        if i % j == 0:
            flag = False
            break
    if flag:
        result.append(i)
print(f"Prime numbers between {start} to {end} is {result}")