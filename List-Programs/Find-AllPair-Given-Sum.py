# Enter the list elements : 2 3 4 5 6 7 7 8
# Enter the target value : 7
# [(2, 5), (3, 4)]

lst = list(map(int,input("Enter the list elements : ").split()))
target = int(input("Enter the target value : "))
result = []
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] + lst[j] == target:
            result.append((lst[i],lst[j]))
print(result)