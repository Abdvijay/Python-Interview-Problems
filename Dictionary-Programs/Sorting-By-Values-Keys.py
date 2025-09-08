# Sort dictionary by keys

# Input: {'c':3, 'a':1, 'b':2}
# Output: {'a':1, 'b':2, 'c':3}

# Sort dictionary by values

# Input: {'apple':10, 'banana':2, 'cherry':5}
# Output: {'banana':2, 'cherry':5, 'apple':10}

import ast
dic = ast.literal_eval(input("Enter the dictionaries : "))
result = dict(sorted(dic.items()))
print(result)

dic = ast.literal_eval(input("Enter the dictionaries : "))
result = dict(sorted(dic.items(), key=lambda x:x[1]))
print(result)