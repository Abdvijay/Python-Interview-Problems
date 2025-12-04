# Input:
# [1, 0, 2, 0, 3, 0, 4]
# Output:
# [1, 2, 3, 4, 0, 0, 0]

lst = list(map(int,input("Enter the list elements : ").split()))
zero_lst = []
result = []
for i in lst:
    if i == 0:
        zero_lst.append(i)
    else:
        result.append(i)
for j in zero_lst:
    result.append(j)
print(f"Result is : {result}")

# Enter the list elements : 1 2 0 4 0 0 8 0
# Result is : [1, 2, 4, 8, 0, 0, 0, 0]