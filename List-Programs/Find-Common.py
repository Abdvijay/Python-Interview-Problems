lst1 = list(map(int,input("Enter the list 1 elements : ").split()))
lst2 = list(map(int,input("Enter the list 2 elements : ").split()))
result = []
for i in lst1:
    for j in lst2:
        if i == j:
            result.append(i)
            break
print(result)