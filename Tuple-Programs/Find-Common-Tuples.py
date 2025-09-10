# Find common tuples between two lists

# Input: [(1,2), (3,4), (5,6)] , [(5,6), (7,8), (1,2)]
# Output: [(1,2), (5,6)]

import ast
tuple1 = ast.literal_eval(input("Enter the list of tuples 1 :"))
tuple2 = ast.literal_eval(input("Enter the list of tuples 2 : "))
result = []
for tup1 in tuple1:
    if tup1 in tuple2:
        result.append(tup1)
print(result)