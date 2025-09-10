# Enter the elements : 1 2 3 4 5 6  
# [1, 3, 5]

lst = list(map(int,input("Enter the elements : ").split()))
odd = [i for i in lst if i % 2 != 0]
print(odd)