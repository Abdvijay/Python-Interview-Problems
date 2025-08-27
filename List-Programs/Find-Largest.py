lst = list(map(int,input("Enter the elements : ").split()))
max = 0
for i in lst:
    if max < i:
        max = i
print(f'Maximum is : {max}')