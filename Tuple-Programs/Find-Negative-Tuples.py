# Find tuples with at least one negative number

# Input: [(-1, 2), (3, 4), (-5, -6), (7, 8)]
# Output: [(-1, 2), (-5, -6)]

import ast
tuples = ast.literal_eval(input("Enter the tuples elements : "))
result = []
for tup in tuples:
    flag = False
    for i in range(len(tup)):
        if tup[i] <= 0:
            flag = True
            break
    if flag:
        result.append(tup)
print(result)