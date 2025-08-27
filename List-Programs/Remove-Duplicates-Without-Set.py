lst = list(map(int,input("Enter the list elements : ").split()))
result = []
for i in lst:
    if i not in result:
        result.append(i)
print(result)