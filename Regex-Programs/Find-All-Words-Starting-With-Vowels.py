# Find all words starting with vowel

# Input: "An elephant is under a tree"
# Output: ['An','elephant','is','under']

import re
string = input("Enter the string : ")
pattern = r'\b[aeiouAEIOU]\w{1,}'
result = re.findall(pattern,string)
print(result)