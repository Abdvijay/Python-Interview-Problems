lst = list(map(int,input("Enter the list elements : ").split()))
target = int(input("Enter the target value : "))
result = []
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] + lst[j] == target:
            result.append((lst[i],lst[j]))
print(result)