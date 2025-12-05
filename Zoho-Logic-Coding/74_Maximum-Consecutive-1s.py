# Input:
# [1, 1, 0, 1, 1, 1, 0, 1]

# Output:
# Maximum consecutive 1’s = 3

lst = list(map(int,input("Enter the list elements : ").split()))
maximum_consecutives = 0
temp = []
for i in lst:
    if i == 1:
        temp.append(i)
    
    if i != 1:
        if maximum_consecutives < len(temp):
            maximum_consecutives = len(temp)
            temp = []

print(f"Maximum consecutive 1's is {maximum_consecutives}")

# Enter the list elements (): 1 4 5 1 1 3 1 1 1 1 5
# Maximum consecutive 1's is 4

# Enter the list elements : 1 1 0 1 1 1 0 1
# Maximum consecutive 1's is 3