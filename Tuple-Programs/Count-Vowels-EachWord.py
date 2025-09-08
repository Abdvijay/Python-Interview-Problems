# Count vowels in each word of a tuple

# Input: ("apple", "banana", "cherry")
# Output: [2, 3, 2]

import ast
tuples = ast.literal_eval(input("Enter the tuples : "))
result = []
for tup in tuples:
    count = 0
    for ch in tup:
        if ch in 'aeiouAEIOU':
            count += 1
    result.append(count)
print(result)