# Enter the elements : 1 2 3 4 5 6
# Enter the value to search : 2
# Value 2 has index of 1

lst = list(map(int,input("Enter the elements : ").split()))
val = int(input("Enter the value to search : "))
if val in lst:
    print(f'Value {val} has index of {lst.index(val)}')