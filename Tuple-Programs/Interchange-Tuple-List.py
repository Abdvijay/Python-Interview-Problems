# Interchange tuples in a list

# Input: [(1, 2), (3, 4), (5, 6)]
# Output: [(2, 1), (4, 3), (6, 5)]

import ast
lst = ast.literal_eval(input("Enter the tuples in a list : "))
result = []
for i in lst:
    lst = list(i)
    lst[0], lst[-1] = lst[-1], lst[0]
    tup = tuple(lst)
    result.append(tup)
print(f'Output : {result}')