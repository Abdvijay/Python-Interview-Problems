lst = list(map(int,input("Enter the list elements : ").split()))
print(f'Before Sorting List : {lst}')
lst.sort(reverse=True)
print(f'After Descending Order : {lst}')