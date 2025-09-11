# Validate email address

# Input: "test.email@example.com"
# Output: Valid

# Input: "test@.com"
# Output: Invalid

import re
email = input("Enter your mail to verify :")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern,email):
    print(f'Your email : {email} is valid')
else:
    print(f'Your email : {email} is not valid')