# Enter the string : hi vijay
# Enter the substring to replace : vijay
# Enter the substring to replacement : preethy
# hi preethy

import re
str = input("Enter the string : ")
replace_for = input("Enter the substring to replace : ")
replacement = input("Enter the substring to replacement : ")
result = re.sub(replace_for,replacement,str)
print(result)