# Extract domain name from email

# Input: "user123@gmail.com"
# Output: "gmail.com"

import re
email = input("Enter the email : ")
pattern = r'@(.+)'
result = re.search(pattern,email)
print(result.group())