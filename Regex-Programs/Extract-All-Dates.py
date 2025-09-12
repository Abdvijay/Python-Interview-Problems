# Extract all dates in format DD/MM/YYYY

# Input: "My birthday is 25/12/2024 and exam is on 01/01/2025"
# Output: ['25/12/2024', '01/01/2025']

import re
string = input("Enter the string : ")
# pattern = r'\b\d{2}\/\d{2}\/\d{4}\b' # It just matches the Date format with simple condition
# pattern = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[12])/(\d{4})\b' # It matches the exact Date format and it avoids un related Dates and it returns the result as a tuple.
pattern = r'\b(?:0[1-9]|[12][0-9]|3[01])/(?:0[1-9]|1[12])/(?:\d{4})\b' # It also same as above but ?: gives the result as Date format result.
result = re.findall(pattern,string)
print(result)