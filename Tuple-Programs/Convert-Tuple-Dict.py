# Convert list of tuples to dictionary

# Input: [("a", 1), ("b", 2), ("c", 3)]
# Output: {'a': 1, 'b': 2, 'c': 3}

import ast
lstoftup = ast.literal_eval(input("Enter the list of tuple : "))
dic = {}
for i in lstoftup:
    dic[i[0]] = i[1]
print(dic)