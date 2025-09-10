# Map words by their last character

# Input: ["cat","bat","dog","frog"]
# Output: {'t':['cat','bat'], 'g':['dog','frog']}

import ast
lst = ast.literal_eval(input("Enter the list of words : "))
result = {}
for word in lst:
    last_letter = word[-1]
    if last_letter not in result:
        result[last_letter] = [word]
    else:
        result[last_letter].append(word)
print(result)