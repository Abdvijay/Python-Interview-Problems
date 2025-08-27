lst = list(map(int,input("Enter the elements : ").split()))
odd = [i for i in lst if i % 2 != 0]
print(odd)