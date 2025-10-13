# Sample Input
# Enter two values separated by space : 5 4

# Sample Output
# Before swapping :  5   4
# After  swapping :  4   5

a,b = list(map(int,input("Enter two values separated by space : ").split()))
print("Before swapping : ",a," ",b)
a = a + b
b = a - b
a = a - b
print("After  swapping : ",a," ",b)