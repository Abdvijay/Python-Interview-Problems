# Find tuple with maximum sum

# Input: [(1,2), (3,4), (5,6)]
# Output: (5,6)

import ast
tuples = ast.literal_eval(input("Enter the tuples : "))
result = []
dic = {}
for tup in tuples:
    sum = 0
    for i in range(len(tup)):
        sum += tup[i]
    dic[sum] = tup
max = max(dic)
print(dic[max])