# Enter the elements : 1 2 3 4 5
# Origin list :  [1, 2, 3, 4, 5]
# Reverse list :  [5, 4, 3, 2, 1]

lst = list(map(int,input("Enter the elements : ").split()))
result = lst[::-1]
print("Origin list : ",lst)
print("Reverse list : ",result)