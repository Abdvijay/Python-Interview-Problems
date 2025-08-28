# Extract digits from tuple elements

# Input: (123, 456, 789)
# Output: [1,2,3,4,5,6,7,8,9]

import ast
tuples = ast.literal_eval(input("Enter the tuple elements : "))
result = []
for data in tuples:
    for i in str(data):
        result.append(i)
print(result)