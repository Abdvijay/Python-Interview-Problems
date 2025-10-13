# Sample Input
# Enter the string one : listen
# Enter the string two : silent

# Sample Output
# The given two string which is listen and silent is Anagrams

string1 = input("Enter the string one : ")
string2 = input("Enter the string two : ")
if sorted(string1) == sorted(string2):
    print(f"The given two string which is {string1} and {string2} is Anagrams")
else:
    print(f"The given two string which is {string1} and {string2} is not an Anagrams")