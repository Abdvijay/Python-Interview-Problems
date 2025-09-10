# Enter the elements : 1 2 3 4 5
# 1

# lst = list(map(int,input("Enter the elements : ").split()))
# small = min(lst)
# print(small)

# or

lst = list(map(int,input("Enter the elements : ").split()))
small = sorted(lst)
print(small[0])