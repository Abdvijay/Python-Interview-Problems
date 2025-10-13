# Sample Input
# Enter the list elements : 1 2 3 1 4 5 6 7 3 4 9 8

# Sample Output
# After removing duplicates [1, 2, 3, 4, 5, 6, 7, 9, 8]

lst = list(map(int,input("Enter the list elements : ").split()))
original = []
for i in lst:
    if i not in original:
        original.append(i)
print(f"After removing duplicates {original}")