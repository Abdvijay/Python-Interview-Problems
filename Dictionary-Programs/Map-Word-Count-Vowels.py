# Map each word to count of vowels in it

# Input: ["apple","banana","dog"]
# Output: {'apple':2, 'banana':3, 'dog':1}

import ast
words = ast.literal_eval(input("Enter the list of words : "))
dic = {}
for word in words:
    count = 0
    for ch in word:
        if ch in 'aeiouAEIOU':
            count += 1
    dic[word] = count
print(dic)