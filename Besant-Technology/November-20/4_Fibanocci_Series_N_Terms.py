n = int(input("Enter the n value : "))
f1,f2 = 0,1
result = [f1,f2]
for i in range(3,n+1):
    f3 = f1 + f2
    result.append(f3)
    f1,f2 = f2,f3
print(f"Fibanocci Series upto N : {result}")

# OUTPUT

# Enter the n value : 5
# Fibanocci Series upto N : [0, 1, 1, 2, 3]