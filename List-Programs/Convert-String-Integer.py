# Sample Input:

# Enter the list elements : 5 8 9 12 2

# Sample Output:

# [5, 8, 9, 12, 2]

lst = list(input("Enter the list elements : ").split())
result = [int(num) for num in lst]
print(result)