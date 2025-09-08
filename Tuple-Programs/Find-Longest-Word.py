# Find the longest word in a tuple

# Input: ("cat", "elephant", "dog", "tiger")
# Output: "elephant"

import ast
tuples = ast.literal_eval(input("Enter the tuples : "))
result = ""
longest = 0
for tup in tuples:
    if longest < len(tup):
        longest = len(tup)
        result = tup
print(f'"{result}"')