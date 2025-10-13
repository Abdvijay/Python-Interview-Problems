# Sample Input
# Enter the start range : 1
# Enter the end range : 30

#Sample Output
# The perfect numbers in range 1, 30 are [6, 28]

start = int(input("Enter the start range : "))
end = int(input("Enter the end range : "))
perfect = []
for i in range(start,end+1):
    temp = []
    for j in range(1,i+1):
        if i % j == 0 and i != j :
            temp.append(j)
    if i == sum(temp):
        perfect.append(i)
print(f"The perfect numbers in range {start}, {end} are {perfect}")