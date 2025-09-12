# Find repeated words in a sentence

# Input: "This is is a test test case"
# Output: ['is','test']

import re
sentence = input("Enter the sentence : ")
pattern = r'\b(\w+)\b\s+\1'
result = re.findall(pattern,sentence,flags=re.IGNORECASE)
print(result)