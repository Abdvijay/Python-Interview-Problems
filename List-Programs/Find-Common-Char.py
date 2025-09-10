# Find common characters in all words

# Input: ["bella","label","roller"]
# Output: ['e','l','l']

import ast
lst = ast.literal_eval(input("Enter the list of words : "))
result = []
flag = False
for ch in lst[0]:
    for word in lst:
        if ch in word:
            flag = True
        else:
            flag = False
    if flag:
            result.append(ch)
print(result)