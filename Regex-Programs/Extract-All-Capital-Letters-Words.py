# Extract all capital words from a sentence

# Input: "I live in NEW YORK and LOVE PYTHON"
# Output: ['NEW', 'YORK', 'LOVE', 'PYTHON']

import re
sentence = input("Enter the sentence : ")
pattern = r'\b[A-Z]{2,}\b'
result = re.findall(pattern,sentence)
print(result)