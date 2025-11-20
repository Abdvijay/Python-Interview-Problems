str1 = input("Enter the string 1 : ")
str2 = input("Enter the string 2 : ")

if sorted(str1) == sorted(str2):
    print(f'The given strings are Anagrams')
else:
    print(f'The given strings are not Anagrams')

# OUTPUT

# Enter the string 1 : cat
# Enter the string 2 : tac
# The given strings are Anagrams

# Enter the string 1 : acd
# Enter the string 2 : acg
# The given strings are not Anagrams