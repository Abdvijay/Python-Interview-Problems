# Find words starting with a given letter

# Input: ("apple", "banana", "avocado", "cherry") → starts with a
# Output: ("apple", "avocado")

import ast
tuples = ast.literal_eval(input("Enter the tuples : "))
letter = input("Enter the one letter : ")
result = []
for tup in tuples:
    if tup[0] == letter:
        result.append(tup)
print(tuple(result))