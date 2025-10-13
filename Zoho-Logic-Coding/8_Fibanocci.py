# Sample Input : 
# Enter the number to find fibanocci series : 5

# Sample Output
# 0 1 1 2 3

number = int(input("Enter the number to find fibanocci series : "))
f1,f2 = 0,1
print(f1,f2,end=" ")
for i in range(2,number):
    f3 = f1 + f2
    print(f3,end=" ")
    f1,f2 = f2,f3