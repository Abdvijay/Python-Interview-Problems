# Replace last element of tuples in a list

# Input: [(1,2,3), (4,5,6), (7,8,9)], replace last with 100
# Output: [(1,2,100), (4,5,100), (7,8,100)]

import ast
tuples = ast.literal_eval(input("Enter the tuples of a list : "))
replaced = int(input("Enter the replacable number : "))
result = []
for tup in tuples:
    lst = list(tup)
    lst[-1] = replaced
    result.append(tuple(lst))
print(result)