# Merge two tuples element-wise into a list of tuples

# Input: (1,2,3) and (4,5,6)
# Output: [(1,4), (2,5), (3,6)]

tup1 = tuple(map(int,input("Enter the tuple 1 elements : ").split()))
tup2 = tuple(map(int,input("Enter the tuple 2 elements : ").split()))
result = []
for i,j in zip(tup1,tup2):
    result.append((i,j))
print(result)