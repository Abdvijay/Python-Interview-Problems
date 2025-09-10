# Enter the list : [[1,2],[3,4,5]]
# [1, 2, 3, 4, 5]

import ast
lst = ast.literal_eval(input("Enter the list : "))
result = [num for sublist in lst for num in sublist]
print(result)