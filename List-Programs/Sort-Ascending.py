# Enter the list elements : 5 4 3 2 1
# Before Sorting : [5, 4, 3, 2, 1]
# Sorting Ascending Order : [1, 2, 3, 4, 5]

lst = list(map(int,input("Enter the list elements : ").split()))
print(f'Before Sorting : {lst}')
lst.sort()
print(f'Sorting Ascending Order : {lst}')