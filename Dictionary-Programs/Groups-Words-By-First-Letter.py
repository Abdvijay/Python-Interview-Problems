# Group words by their first letter

# Input: ["cat", "car", "dog", "door", "apple"]
# Output: {'c': ['cat', 'car'], 'd': ['dog', 'door'], 'a': ['apple']}

import ast
lst = ast.literal_eval(input("Enter the list of words : "))
dic = {}
for word in lst:
    key = word[0]
    if key not in dic:
        dic[key] = [word]
    else:
        dic[key].append(word)
print(dic)