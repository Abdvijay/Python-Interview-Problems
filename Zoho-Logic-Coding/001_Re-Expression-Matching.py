import re
string = input("Enter the string : ")
pattern = input("Enter the pattern : ")
result = re.fullmatch(pattern,string) is not None
print(result)

# # SAMPLE INPUT AND SAMPLE OUTPUT 1
# Enter the string : aa
# Enter the pattern : a
# False

# # SAMPLE INPUT AND SAMPLE OUTPUT 2
# Enter the string : aa
# Enter the pattern : a*
# True

# # SAMPLE INPUT AND SAMPLE OUTPUT 3
# Enter the string : ab
# Enter the pattern : a.*
# True