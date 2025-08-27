str = input("Enter the string : ")
lst = []
for i in str:
    count = 0
    for j in str:
        if i == j:
            count += 1
    if count <= 1:
        lst.append(i)
print(lst[0])