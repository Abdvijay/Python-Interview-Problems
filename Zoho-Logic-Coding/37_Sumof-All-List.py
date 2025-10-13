# Sample Input
# Enter the list elements : 2 5 3 1 4

# Sample Output
# The sum of all list elements [2, 5, 3, 1, 4] is 15

lst = list(map(int,input("Enter the list elements : ").split()))
total = 0
for i in lst:
    total += i
print(f"The sum of all list elements {lst} is {total}")