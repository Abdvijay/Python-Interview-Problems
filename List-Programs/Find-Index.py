lst = list(map(int,input("Enter the elements : ").split()))
val = int(input("Enter the value to search : "))
if val in lst:
    print(f'Value {val} has index of {lst.index(val)}')