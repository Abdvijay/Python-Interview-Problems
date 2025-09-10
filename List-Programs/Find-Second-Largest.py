# Enter the elements : 1 2 3 4 5
# 4

lst = list(map(int,input("Enter the elements : ").split()))
sorted_lst = sorted(set(lst),reverse=True)
print(sorted_lst[1])