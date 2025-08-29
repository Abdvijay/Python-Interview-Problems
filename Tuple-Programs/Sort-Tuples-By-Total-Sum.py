# Sort list of tuples by total sum of elements

# Input: [(1,2), (2,3), (4,1)]
# Output: [(1,2), (4,1), (2,3)]

# (Sums → 3, 5, 5 → sorted)

import ast

tuples = ast.literal_eval(input("Enter the tuples : "))
result = sorted(tuples, key=lambda x: sum(x))
print(result)