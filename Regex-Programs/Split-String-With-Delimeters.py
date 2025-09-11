# Split string by multiple delimiters (, ; |)

# Input: "apple;banana,grape|orange"
# Output: ['apple','banana','grape','orange']

import re
string = input("Enter the string : ")
pattern = r'[:,;| ]+'
result = re.split(pattern,string)
print(result)