# Create a dictionary from two lists

# Input: keys = ["a", "b", "c"], values = [1, 2, 3]
# Output: {'a': 1, 'b': 2, 'c': 3}

import ast
keys = ast.literal_eval(input("Enter the keys : "))
values = ast.literal_eval(input("Enter the values : "))
dic = dict(zip(keys,values))
print(dic)