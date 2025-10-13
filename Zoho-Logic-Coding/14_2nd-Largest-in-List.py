# Sample input
# Enter the number in list : 1 2 3 4 5

# Sample Output
# The 2nd Largest Number of [1, 2, 3, 4, 5] is 4

number = list(map(int,input("Enter the number in list : ").split()))
number.sort()
print(f"The 2nd Largest Number of {number} is {number[-2]}")