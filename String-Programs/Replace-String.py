import re
str = input("Enter the string : ")
replace_for = input("Enter the substring to replace : ")
replacement = input("Enter the substring to replacement : ")
result = re.sub(replace_for,replacement,str)
print(result)