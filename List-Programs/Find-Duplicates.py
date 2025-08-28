# Find duplicate elements in a list

# Input: [1, 2, 3, 2, 4, 5, 1]
# Output: [1, 2]

lst = list(map(int,input("Enter the list elements : ").split()))
repeat = []
# result = []
# for i in lst:
#     if i not in result:
#         result.append(i)
#     else:
#         repeat.append(i)
# print("Duplicates elements : ",repeat)

for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] == lst[j] and lst[i] not in repeat:
            repeat.append(lst[i])
            break
print("Duplicates elements : ",repeat)