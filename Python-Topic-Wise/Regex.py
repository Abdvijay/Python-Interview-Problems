import re

str = "hi vijay this is my dob 13/11/2000"
pattern = r'hi'
result = re.match(pattern,str)
print("1. Regex match                             : ",result) # match → Tries to match the pattern only at the beginning of the string.

pattern = r'is'
result = re.search(pattern,str)
print("2. Regex search                            : ",end= " ") # Searches the string for the first occurrence of the pattern (anywhere).
if result:
    print("[ Matched object : ",result.group(),end=" ], ")
    print("[ Starting position : ",result.start(),end="], ")
    print("[ Ending position : ",result.end(),end="] \n")

names = "laksh vijay;swathi+dhansika deeksha_raman"
pattern = r'[ ;,_+=]'
result = re.split(pattern,names)
print("3. Regex split                             : ",result) # Splits the string by the regex pattern.

sentence = "Hi vijay this so so good and i know it is good."
result = re.sub('good','bad',sentence)
print("4. Regex sub                               : ",result) # Replaces all occurrences of pattern with repl.

sentence = "Hi i'm vijay my dob is 13/11/2000"
pattern = r'\d+'
result = list(re.finditer(pattern,sentence)) # when you need all matches with details (like positions, groups).
print("5. Regex finditer                          : ",end=" ")
print("[ Matched object : ",[i.group() for i in result],end=" ], ")
print("[ Starting position : ",[i.start() for i in result],end="], ")
print("[ Ending position : ",[i.end() for i in result],end="] \n")

sentence = "Hi vijay this so so good and i know it is good."
pattern = r'good'
result = re.findall(pattern,sentence)
print("6. Regex findall                           : ",result) # when you need all matches (but just the values).

tweet = "Hi this post represents nature #Beautiful #Nature"
pattern = r'#\w+'
result = re.findall(pattern,tweet)
print("7. Fetching hashtag (check with #)         : ",result)

pattern = r'\b\w+s\b'
result = re.findall(pattern,tweet)
print("8. Fetching words ending with s            : ",result)

mail = 'abdvijay1923@gmail.com'
pattern = r'@(.+)'
result = re.findall(pattern,mail)
print("9. Fetching domain name only               : ",result)

sentence = "I think elephant is an big animal"
pattern = r'\b[aeiouAEIOU]\w{1,}'
result = re.findall(pattern,sentence)
print("10. Finding all words starting with vowels : ",result)

sentence = "This is a test test case"
pattern = r'\b(\w+)\b\s+\1'
result = re.findall(pattern,sentence,flags=re.IGNORECASE)
print("11. Printing repeated value only           : ",result)

pattern = r'^[\w\.\_]+@[\w\.\_]+\.\w+$'
result = re.findall(pattern,mail)
print("12. Check valid mail or not                : ",[f"Valid email        -> {result}" if result else "Not Valid"])

phone_number = "+91 94283 78392"
pattern = r'^\+\d{1,3}[ -]?\d{5}[\s]\d{5}'
result = re.findall(pattern,phone_number)
print("13. Check valid phone number or not        : ",[f"Valid phone number -> {result}" if result else "Not Valid"])

word = "hello"
pattern = r'^[a-zA-Z]+$'
result = re.findall(pattern,word)
print("14. Check the word is only alphabet or not : ",[f"Only Alphabets     -> {result}" if result else "Not only alphabets"])

sentence = "HI this is VIJAY from NELLAI"
pattern = r'\b[A-Z]+\b'
result = re.findall(pattern,sentence)
print("15. Finding fully capitalized words only   : ",result)

sentence = "This is my course joining date -> 04/09/2023 and completed at 16/06/2025"
pattern = r'\b(?:0[1-9]|[12][0-9]|3[01])/(?:0[1-9]|1[12])/(?:\d{4})\b'
result = re.findall(pattern,sentence)
print("16. Finding date formats only              : ",result)

sentence = "hi this is vijay and i'm 24 years old and this is 17th question"
pattern = r'\d{1,}'
result = re.findall(pattern,sentence)
print("17. Finding numeric values only            : ",result)

sentence = "now time is 17:05 but i found answer at 17:10"
pattern = r'\b(?:[01][0-9]|2[0-4]):(?:[0-5][0-9]|60)\b'
result = re.findall(pattern,sentence)
print("18. Finding times values only              : ",result)