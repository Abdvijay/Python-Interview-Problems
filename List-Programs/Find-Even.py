# Enter the elements : 1 2 3 4 5 6
# [2, 4, 6]

lst = list(map(int,input("Enter the elements : ").split()))
even = [i for i in lst if i % 2 == 0]
print(even)