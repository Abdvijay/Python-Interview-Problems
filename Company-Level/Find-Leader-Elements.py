lst = list(map(int,input("Enter the list elements : ").split()))
result = []
for i in range(0,len(lst)):
    flag = True
    for j in range(i+1,len(lst)):
        if lst[i] > lst[j]:
            flag = True
        else:
            flag = False
            break
    if flag:
        result.append(lst[i])
print(f'Leader Elements : {result}')