# Remove a key from dictionary

# Input: {'a':1, 'b':2, 'c':3}, remove 'b'
# Output: {'a':1, 'c':3}

import ast
dic = ast.literal_eval(input("Enter the dictionaries : "))
rem = input("Enter the removable key : ")
del dic[rem]
print(dic)