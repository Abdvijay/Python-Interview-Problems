# Extract time in HH:MM format

# Input: "The train leaves at 09:45 and arrives at 18:30"
# Output: ['09:45','18:30']

import re
string = input("Enter the string : ")
pattern = r'\b(?:[01][0-9]|2[0-4]):(?:[0-5][0-9]|60)\b'
result = re.findall(pattern,string)
print(result)