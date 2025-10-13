# Sample Input
# Enter the list 1 elements : 1 5 4 3 2
# Enter the list 2 elements : 6 8 7 9 0

# Sample Output
# After merging two list : [1, 5, 4, 3, 2, 6, 8, 7, 9, 0]
# After sorting          : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst1 = list(map(int,input("Enter the list 1 elements : ").split()))
lst2 = list(map(int,input("Enter the list 2 elements : ").split()))

merged = lst1 + lst2
print(f"After merging two list : {merged}")
for i in range(len(merged)):
    for j in range(0,len(merged)-i-1):
        if merged[j] > merged[j+1]:
            merged[j], merged[j + 1] = merged[j + 1], merged[j]
print(f"After sorting          : {merged}")