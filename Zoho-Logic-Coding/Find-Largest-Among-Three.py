# Sample Input
# Enter three numbers (Enter values by space) : 5 4 6

# Sample Output
# Largest number is  6

numbers = list(map(int,input("Enter three numbers (Enter values by space) : ").split()))
numbers.sort()
print("Largest number is ",numbers[-1])