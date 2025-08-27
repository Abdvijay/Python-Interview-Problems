lst = list(map(int,input("Enter the elements : ").split()))
product = 1
[product := product * i for i in lst]
print(product)