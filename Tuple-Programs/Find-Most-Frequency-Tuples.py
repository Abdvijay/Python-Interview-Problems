# Find the most frequent tuple in list

# Input: [(1,2), (3,4), (1,2), (1,2), (5,6)]
# Output: (1,2)

import ast
tuples = ast.literal_eval(input("Enter the tuples : "))
result = {}
for tup in tuples:
    if tup in result:
        result[tup] += 1
    else:
        result[tup] = 1
max = 0
for key,value in result.items():
    if max < value:
        max = value
for key,value in result.items():
    if max == value:
        print(key)