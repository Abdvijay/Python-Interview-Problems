# Sample Input
# Enter the number to check odd or even : 4

# Sample Output
# The given number 4 is Even

num = int(input("Enter the number to check odd or even : "))
check_odd_even = lambda x : "Even" if x % 2 == 0 else "Odd"
print(f"The given number {num} is {check_odd_even(num)}")