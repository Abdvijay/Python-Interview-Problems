str = input("Enter the string : ")
lst = []
for i in str:
    if i in lst:
        pass
    else:
        lst.append(i)
print(''.join(lst))