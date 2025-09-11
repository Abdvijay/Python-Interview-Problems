# Check if string contains only alphabets

# Input: "HelloWorld" → True
# Input: "Hello123" → False

import re
string = input("Enter the string : ")
pattern = r'^[a-zA-Z]+$'
result = re.fullmatch(pattern,string)
if result:
    print("True")
else:
    print("False")