# Enter the list 1 elements : 1 2 3 4
# Enter the list 2 elements : 2 3 4 5
# [1, 2, 3, 4, 2, 3, 4, 5]

lst1 = list(map(int,input("Enter the list 1 elements : ").split()))
lst2 = list(map(int,input("Enter the list 2 elements : ").split()))
result = lst1 + lst2
print(result)