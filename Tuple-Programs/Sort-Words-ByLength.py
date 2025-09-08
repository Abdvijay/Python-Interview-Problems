# Sort words in a tuple by length

# Input: ("python", "java", "c", "golang")
# Output: ("c", "java", "golang", "python")

import ast
tuples = ast.literal_eval(input("Enter the tuples : "))
result = tuple(sorted(tuples,key=len))
print(result)