# Input:
# [1, 5, 10, 20]
# [5, 20, 30, 40]
# [5, 6, 20, 80]

# Output:
# [5, 20]

list1 = list(map(int,input("Enter the list 1 elements : ").split()))
list2 = list(map(int,input("Enter the list 2 elements : ").split()))
list3 = list(map(int,input("Enter the list 3 elements : ").split()))

# Method 1 - Normal Way
# result = []
# for i in list1:
#     for j in list2:
#         if i == j:
#             for k in list3:
#                 if i == k:
#                     result.append(i)

# Method 2 - Using List Comprehension
# result = [i for i in list1 if i in list2 and i in list3]

# Method 3 - Using Set Methods
result = sorted(list(set(list1) & set(list2) & set(list3)))

print(f'Common elements is {result}')