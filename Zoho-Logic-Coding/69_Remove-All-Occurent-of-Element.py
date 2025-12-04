# Input:
# List: [1, 2, 3, 2, 4, 2]
# Element to remove: 2

# Output:
# [1, 3, 4]

lst = list(map(int,input("Enter the list elements : ").split()))
element = int(input("Enter the element to remove : "))
# result = []
# for i in lst:
#     if i != element:
#         result.append(i)

result = [i for i in lst if i != element]

print(f"After removing all occurrences of the element : {result}")