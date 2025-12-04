# Input:
# [1, 2, 3, 2, 1, 4, 5]

# Output:
# [3, 4, 5]

lst = list(map(int,input("Enter the list elements : ").split()))
result = []
temp = {}
for i in lst:
    if i not in temp:
        temp[i] = 1
    else:
        temp[i] += 1
for key,value in temp.items():
    if value == 1:
        result.append(key)
print(f'Unique Element : {result}')

# Sample Example - 1
# Enter the list elements : 1 2 3 2 1 4 5
# Unique Element : [3, 4, 5]

# Sample Example - 2
# Enter the list elements : 1 2 3 4 5
# Unique Element : [1, 2, 3, 4, 5]