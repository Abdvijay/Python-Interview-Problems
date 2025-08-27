number = int(input("Enter the number : "))
f1, f2 = 0, 1
result = [f1, f2]
for i in range(2,number):
    f3 = f1 + f2
    result.append(f3)
    f1 = f2
    f2 = f3
print(result)