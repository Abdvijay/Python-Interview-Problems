lst = list(map(int,input("Enter the list elements : ").split()))
result = []
for i in range(1,lst[-1]):
    if i not in lst:
        result.append(i)
print(f'Missing number : {result}')