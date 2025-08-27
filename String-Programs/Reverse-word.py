str = list(input("Enter the string : ").split())
lst = []
for i in range(len(str)-1,-1,-1):
    lst.append(str[i])
print(' '.join(lst))