# Find words ending with a given letter

# Input: ("king", "ring", "cat", "dog") → ends with g
# Output: ("king", "ring", "dog")

# import ast
# tuples = ast.literal_eval(input("Enter the tuples : "))
# letter = input("Enter the letter : ")
# result = []
# for tup in tuples:
#     if tup[-1] == letter:
#         result.append(tup)
# print(tuple(result))

import ast
tuples = ast.literal_eval(input("Enter the tuples : "))
letter = input("Enter the letter : ")
result = tuple(word for word in tuples if word.endswith(letter))
print(result)