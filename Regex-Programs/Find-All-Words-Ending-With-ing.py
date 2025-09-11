# Find all words ending with 'ing'

# Input: "I am running and eating while coding"
# Output: ['running','eating','coding']

import re
string = input("Enter the string : ")
pattern = r'\b\w+ing\b'
result = re.findall(pattern,string)
print(result)