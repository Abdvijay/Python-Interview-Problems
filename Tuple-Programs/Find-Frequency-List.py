# Find frequency of tuples inside list

# Input: [(1,2), (3,4), (1,2), (5,6), (1,2)]
# Output: {(1,2): 3, (3,4): 1, (5,6): 1}

import ast
tuples = ast.literal_eval(input("Enter the tuples inside list : "))
dic = {}
for tuple in tuples:
    if tuple in dic:
        dic[tuple] += 1
    else:
        dic[tuple] = 1
print(dic)