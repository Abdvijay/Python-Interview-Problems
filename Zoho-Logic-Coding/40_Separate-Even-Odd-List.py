# Sample Input
# Enter the list elements : 1 2 3 4 5

# Sample Output
# Odd elements list [1, 3, 5] and Even elements list [2, 4]

lst = list(map(int,input("Enter the list elements : ").split()))
even = [x for x in lst if x % 2 == 0]
odd = [x for x in lst if x % 2 != 0]
print(f"Odd elements list {odd} and Even elements list {even}")