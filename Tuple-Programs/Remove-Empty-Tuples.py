# Remove empty tuples from list

# Input: [(), (1,2), (), (3,4), (5,)]
# Output: [(1,2), (3,4), (5,)]

import ast
tuples = ast.literal_eval(input("Enter the tuples : "))
result = []
for i in tuples:
    if i:
        result.append(i)
print(result)