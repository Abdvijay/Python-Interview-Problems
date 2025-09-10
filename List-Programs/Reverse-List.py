# Enter the list elements : 1 2 3 4 5
# Before reverse : [1, 2, 3, 4, 5]
# After reverse : [5, 4, 3, 2, 1]

lst = list(map(int,input("Enter the list elements : ").split()))
print(f'Before reverse : {lst}')
lst.reverse()
print(f'After reverse : {lst}')