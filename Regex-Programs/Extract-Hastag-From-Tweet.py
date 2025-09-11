# Extract hashtags from a tweet

# Input: "I love #Python and #MachineLearning"
# Output: ['#Python','#MachineLearning']

import re
string = input("Enter the string : ")
pattern = r'#\w+'
result = re.findall(pattern,string)
print(result)