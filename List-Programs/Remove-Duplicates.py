# Enter the elements : 1 2 2 3 3 4 4 5
# Original List Elements :  [1, 2, 2, 3, 3, 4, 4, 5]
# After Removing Duplicate :  {1, 2, 3, 4, 5}

lst = list(map(int,input("Enter the elements : ").split()))
result = set(lst)
print("Original List Elements : ",lst)
print("After Removing Duplicate : ",result)