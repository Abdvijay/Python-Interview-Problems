# Sort words in a tuple alphabetically

# Input: ("banana", "apple", "cherry")
# Output: ("apple", "banana", "cherry")

import ast
tuples = ast.literal_eval(input("Enter the tuples : "))
lst = list(tuples)
lst.sort()
print(tuple(lst))