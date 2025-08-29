# Find repeated tuples in a list

# Input: [(1,2), (3,4), (1,2), (5,6), (3,4)]
# Output: [(1,2), (3,4)]

import ast
tuples = ast.literal_eval(input("Enter the list of tuples : "))
result = []
repeat = []
for tup in tuples:
    if tup not in result:
        result.append(tup)
    else:
        repeat.append(tup)
print(repeat)