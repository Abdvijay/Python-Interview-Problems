# Enter two words separated by space: listen netsil
# The given strings are Anagrams

words = input("Enter two words separated by space: ").split()

if len(words[0]) != len(words[1]):
    print("The given strings are NOT Anagrams")
else:
    if sorted(words[0]) == sorted(words[1]):
        print("The given strings are Anagrams")
    else:
        print("The given strings are NOT Anagrams")