# Combine dictionaries adding values for common keys

# Input: {'a':10, 'b':20}, {'a':5, 'c':30}
# Output: {'a':15, 'b':20, 'c':30}

import ast
dic1 = ast.literal_eval(input("Enter the dictionary one : "))
dic2 = ast.literal_eval(input("Enter the dictionary two : "))
for keys,values in dic2.items():
    if keys not in dic1:
        dic1[keys] = values
    else:
        dic1[keys] = dic1[keys] + values
print(dic1)