# Reverse dictionary (swap keys and values)

# Input: {'a':1, 'b':2, 'c':3}
# Output: {1:'a', 2:'b', 3:'c'}

import ast
dic = ast.literal_eval(input("Enter the dictionary : "))
result = {}
for keys,values in dic.items():
    if values not in result:
        result[values] = [keys]
    else:
        result[values].append(keys)
print(result)