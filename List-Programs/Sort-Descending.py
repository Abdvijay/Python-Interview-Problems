# Enter the list elements : 1 2 3 4 5
# Before Sorting List : [1, 2, 3, 4, 5]
# After Descending Order : [5, 4, 3, 2, 1]

lst = list(map(int,input("Enter the list elements : ").split()))
print(f'Before Sorting List : {lst}')
lst.sort(reverse=True)
print(f'After Descending Order : {lst}')