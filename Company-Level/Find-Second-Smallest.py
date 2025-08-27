# Find Second Smallest Number in List

# Input: [12, 4, 9, 1, 15]

# Output: 4

lst = list(map(int,input("Enter the list elements : ").split()))
lst.sort()
print(f'The second smallest element is {lst[1]}')