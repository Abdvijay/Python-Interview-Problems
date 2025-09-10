# Enter the elements : 2 4 2 8 6 4 2 6

# {2: 3, 4: 2, 8: 1, 6: 2}


lst = list(map(int,input("Enter the elements : ").split()))
dict = {}
for i in lst:
    count = 0
    for j in lst:
        if i == j:
            count += 1
    dict[i] = count
print(dict)