# Sample Input
# Enter the list of numbers : 1 2 3 1 2 4 5    

# Sample Output
# The list [1, 2, 3, 1, 2, 4, 5] has these duplicate elements [1, 2]

# lst = list(map(int,input("Enter the list of numbers : ").split()))
# dic = {}
# result = []
# for i in lst:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1
# for i in dic.keys():
#     if dic[i] > 1:
#         result.append(i)
# print(f"The list {lst} has these duplicate elements {result}")

lst = list(map(int,input("Enter the list elements : ").split()))
dup = []
without_dup = []
for i in lst:
    if i not in without_dup:
        without_dup.append(i)
    else:
        dup.append(i)
print(f"The list {lst} has these duplicate elements {dup}")