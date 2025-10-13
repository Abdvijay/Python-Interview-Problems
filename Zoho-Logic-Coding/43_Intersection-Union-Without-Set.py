# Sample Input
# Enter the list 1 elements : 1 2 3 4 5
# Enter the list 2 elements : 4 5 6 7 8

# Sample Output
# Union [1, 2, 3, 4, 5, 4, 5, 6, 7, 8]
# Intersection [4, 5]

lst1 = list(map(int,input("Enter the list 1 elements : ").split()))
lst2 = list(map(int,input("Enter the list 2 elements : ").split()))

intersection = []
for i in lst1:
    for j in lst2:
        if i == j:
            intersection.append(i)

union = [x for x in lst1]
for i in lst2:
    union.append(i)
print(f"Union {union}")
print(f"Intersection {intersection}")