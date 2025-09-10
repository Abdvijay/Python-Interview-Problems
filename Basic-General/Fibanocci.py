# Enter the number : 5
# 0 1 1 2 3

num = int(input("Enter the number : "))
f1,f2 = 0,1
print(f1, f2, end=" ")
for i in range(2,num):
    f3 = f1 + f2
    print(f3, end=" ")
    f1 = f2
    f2 = f3