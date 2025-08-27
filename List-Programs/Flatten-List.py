import ast
lst = ast.literal_eval(input("Enter the list : "))
result = [num for sublist in lst for num in sublist]
print(result)