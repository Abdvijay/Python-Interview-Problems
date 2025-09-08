# Find key with maximum value

# Input: {'a':10, 'b':20, 'c':5}
# Output: 'b'

import ast
dic = ast.literal_eval(input("Enter the dictionary : "))
result = []
maximum = 0
for keys,values in dic.items():
    if maximum < values:
        maximum = values
for keys,values in dic.items():
    if maximum == values:
        result.append(keys)
print(result)