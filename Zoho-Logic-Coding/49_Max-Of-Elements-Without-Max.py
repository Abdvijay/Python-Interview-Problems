# Sample Input
# Enter the list elements : 1 2 3 5 42 64 21 76 43 232

# Sample Output
# The maximum of [1, 2, 3, 5, 42, 64, 21, 76, 43, 232] is 232

lst = list(map(int,input("Enter the list elements : ").split()))
max = lst[0]
for i in lst:
    if i > max:
        max = i
print(f"The maximum of {lst} is {max}")