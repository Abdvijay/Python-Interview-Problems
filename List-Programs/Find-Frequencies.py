lst = list(map(int,input("Enter the elements : ").split()))
dict = {}
for i in lst:
    count = 0
    for j in lst:
        if i == j:
            count += 1
    dict[i] = count
print(dict)