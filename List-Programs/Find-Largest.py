# Enter the elements : 1 2 4 6 7 35 32
# Maximum is : 35

lst = list(map(int,input("Enter the elements : ").split()))
max = 0
for i in lst:
    if max < i:
        max = i
print(f'Maximum is : {max}')