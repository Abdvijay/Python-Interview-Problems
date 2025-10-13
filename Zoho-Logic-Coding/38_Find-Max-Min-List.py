lst = list(map(int,input("Enter the list elements : ").split()))
lst.sort()
print(f"The maximum of {lst} is {lst[-1]}")
print(f"The minimum of {lst} is {lst[0]}")