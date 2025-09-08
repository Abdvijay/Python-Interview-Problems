# Find palindrome words in a tuple

# Input: ("level", "python", "madam", "world")
# Output: ("level", "madam")

import ast
tuples = ast.literal_eval(input("Enter the tuples : "))
result = []
for tup in tuples:
    if tup == tup[::-1]:
        result.append(tup)
print(tuple(result))