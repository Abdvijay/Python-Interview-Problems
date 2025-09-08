# Get dictionary items as list of tuples

# Input: {'x':1, 'y':2}
# Output: [('x',1), ('y',2)]

import ast
dic = ast.literal_eval(input("Enter the dictionary : "))
result = []
for keys,values in dic.items():
    result.append((keys,values))
print(result)