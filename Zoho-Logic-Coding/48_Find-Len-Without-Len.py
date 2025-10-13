# Sample Input
# Enter the list elements : 1 2 4 6 2 

# Sample Output
# The length of list elements [1, 2, 4, 6, 2] is 5

lst = list(map(int,input("Enter the list elements : ").split()))
count = 0
for i in lst:
    count += 1
print(f"The length of list elements {lst} is {count}")