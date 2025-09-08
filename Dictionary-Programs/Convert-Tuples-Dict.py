# Convert list of tuples into dictionary

# Input: [("name","Vijay"), ("age",22)]
# Output: {'name':'Vijay', 'age':22}

import ast
tuples = ast.literal_eval(input("Enter the list of tuples : "))
result = {}
for tup in tuples:
    result[tup[0]] = tup[1]
print(result)