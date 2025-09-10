# Enter the list 1 elements : 2 4 6 8 10
# Enter the list 2 elements : 3 6 9 12 4 8

# [4, 6, 8]

lst1 = list(map(int,input("Enter the list 1 elements : ").split()))
lst2 = list(map(int,input("Enter the list 2 elements : ").split()))
result = []
for i in lst1:
    for j in lst2:
        if i == j:
            result.append(i)
            break
print(result)