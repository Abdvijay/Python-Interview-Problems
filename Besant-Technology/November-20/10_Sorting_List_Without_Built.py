lst = list(map(int,input("Enter the list elements by space : ").split()))
print(f'Before sorting : {lst}')
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] > lst[j]:
            lst[i],lst[j] = lst[j],lst[i]
print(f'After sorting : {lst}')


# OUTPUT

# Enter the list elements by space : 1 4 6 3 6 8 3
# Before sorting : [1, 4, 6, 3, 6, 8, 3]
# After sorting : [1, 3, 3, 4, 6, 6, 8]

# Enter the list elements by space : 5 4 3 2 1
# Before sorting : [5, 4, 3, 2, 1]
# After sorting : [1, 2, 3, 4, 5]