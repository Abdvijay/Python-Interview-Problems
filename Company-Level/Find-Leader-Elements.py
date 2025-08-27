# Find Leader Elements in Array

# (Element is leader if no element on its right is greater)

# Input: [16, 17, 4, 3, 5, 2]

# Output: [17, 5, 2]


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