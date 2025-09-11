# Extract all numbers from a string

# Input: "My marks are 75 in math, 88 in science, and 92 in English."
# Output: [75, 88, 92]

import re
string = input("Enter the string : ")
pattern = r'[\d]+'
# result = re.finditer(pattern,string)
# for res in result:
#     print(f'Values : {res.group()}')
#     print(f'Starting From : {res.start()} Position')
#     print(f'Ending At : {res.end()} Position')

result = re.findall(pattern,string)
print(result)