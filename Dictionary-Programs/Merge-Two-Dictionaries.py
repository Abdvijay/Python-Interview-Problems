# Merge two dictionaries

# Input: {'a': 1, 'b': 2} , {'c': 3, 'd': 4}
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

import ast
dict1 = ast.literal_eval(input("Enter the dictionary one : "))
dict2 = ast.literal_eval(input("Enter the dictionary two : "))
# for keys,values in dict2.items():
#     if keys not in dict1:
#         dict1[keys] = values
# print(dict1)
merged = {**dict1, **dict2}
print(merged)