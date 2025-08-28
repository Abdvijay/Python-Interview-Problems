# Flatten a list of tuples into a single list

# Input: [(1,2), (3,4), (5,6)]
# Output: [1,2,3,4,5,6]

import ast
tuples = ast.literal_eval(input("Enter the list of tuples : "))
result = [data for tup in tuples for data in tup]
print(result)