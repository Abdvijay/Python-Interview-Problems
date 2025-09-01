# Split tuple into two lists

# Input: [(1, 'a'), (2, 'b'), (3, 'c')]
# Output: [1,2,3] , ['a','b','c']

import ast
tuples = ast.literal_eval(input("Enter the tuples elements : "))
keys = []
values = []
for key,value in tuples:
    keys.append(key)
    values.append(value)
print(f'{keys} , {values}')