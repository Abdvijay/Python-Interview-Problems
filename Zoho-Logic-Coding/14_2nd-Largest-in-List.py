# Sample input
# Enter the number in list : 1 2 3 4 5

# Sample Output
# The 2nd Largest Number of [1, 2, 3, 4, 5] is 4

# Enter the number in list : 1 4 3 5 2
# Enter the k th position : 1
# The 2nd Largest Number of [1, 2, 3, 4, 5] is 5

number = list(map(int,input("Enter the number in list : ").split()))
k = int(input("Enter the k th position : "))
number.sort()
print(f"The 2nd Largest Number of {number} is {number[-k]}")