lst1 = list(map(int,input("Enter the list 1 elements : ").split()))
lst2 = list(map(int,input("Enter the list 2 elements : ").split()))
result = []
for i in lst1:
    flag = False
    for j in lst2:
        if i == j:
            flag = True
    if not flag:
        result.append(i)
print(result)