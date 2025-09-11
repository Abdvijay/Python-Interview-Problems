# Validate mobile number (10 digits only)

# Input: "9876543210"
# Output: Valid

# Input: "12345"
# Output: Invalid

import re
mobile_number = input("Enter the mobile number : ")
pattern = r'\d{10}'
# pattern = r'^\+\d{1,3}[- ]?\d{7,12}$' it uses the country code programs
if re.match(pattern,mobile_number):
    print(f'Your mobile number : {mobile_number} is valid')
else:
    print(f'Your mobile number : {mobile_number} is not valid')