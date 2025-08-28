# Find tuples with all positive numbers

# Input: [(-1, 2), (3, 4), (0, 5), (6, 7)]
# Output: [(3, 4), (6, 7)]

import ast
tuples = ast.literal_eval(input("Enter the tuples of list : "))
result = []
for tup in tuples:
    flag = True
    for i in range(len(tup)):
        if tup[i] <= 0:
            flag = False
            break
    if flag:
        result.append(tup)
print(result)