# Enter the list elements : 1 2 2 3 4 4 5
# [1, 2, 3, 4, 5]

lst = list(map(int,input("Enter the list elements : ").split()))
result = []
for i in lst:
    if i not in result:
        result.append(i)
print(result)