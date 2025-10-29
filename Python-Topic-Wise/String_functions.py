print("1. upper()         - ","vijay".upper()) #Converts a string into uppercase
print("2. lower()         - ","VIJAY".lower()) #Converts a string into lowercase
print("3. title()         - ","vijay is the best".title()) #Converts each word first letter into uppercase
print("4. capitalize()    - ","vijay is the best".capitalize()) #Converts a sentence's first letter into uppercase
print("5. strip()         - ","----vijay**$$".strip("-*$")) #Removes all spaces
print("6. lstrip()        - ","-----vijay-----".lstrip("-")) #Removes specified left characters
print("7. rstrip()        - ","-----vijay-----".rstrip("-")) #Removes specified right characters
print("8. startswith()    - ","hi hello everyone".startswith("hi")) #Check with mentioned char is starting or not and return boolean
print("9. endswith()      - ","i'm enjoying".endswith("ing")) #Check with mentioned char is ending or not and return boolean
print("10. replace()      - ","Hi good morning all".replace("morning","evening")) #Replace the existing word with new word
print("11. swapcase()     - ","Hi vijay How Are you ?".swapcase()) #Converts all uppercase into and lowercase into uppercase
print("12. join()         - ","-".join(['a','b','c'])) #Joins all the strings with the specified char
print("13. split()        - ","Hi_guys_how_are_you ? ".split("_")) #Split into a list
print("14. find()         - ","program".find("r")) #Find and return the index of first matches and return -1 if not found
print("15. index()        - ","program".index("r")) #Find and return the index of first matches and throw error if not found
print("16. count()        - ","appa".count("a")) #Count the specified char and return
print("17. rfind()        - ","program".rfind("a")) #Find and return the last occurence of match word
print("18. zfill()        - ","42".zfill(5)) #Pads with zero
print("19. center()       - ","53".center(10,"%")) #Centers a string with specified char
print("20. rjust()        - ","67".rjust(10,"$")) #Right align with the specified char
print("21. ljust()        - ","89".ljust(10,"#")) #Left align with the specified char
print("22. islower()      - ","vijay".islower()) #Check if the string is fully lowercase or not and return as boolean value
print("23. isupper()      - ","VIJAY".isupper()) #Check if the string is fully uppercase or not and return as boolean value
print("24. isalpha()      - ","python".isalpha()) #Check if the string is fully alphabets or not and return as boolean value
print("25. isalnum()      - ","python123".isalnum()) #Check if the string is fully alphanumeric or not and return as boolean value
print("26. isdigit()      - ","9080".isdigit()) #Check if the string is fully digit only or not and return as boolean value
print("27. isspace()      - "," ".isspace()) #Check if the string is space or not and return as boolean value
print("28. istitle()      - ","Hi Vijay".istitle()) #Check if the string is satisfied titlecase or not and return as boolean value
print("29. isnumeric()    - ","²³".isnumeric()) #Check if the string is any kind of numbers(fraction,superscript,symbols)
print("30. removeprefix() - ","string_methods.py".removeprefix("string_methods")) #Removes a specific prefix if it exists.
print("31. removesuffix() - ","string_methods.py".removesuffix(".py")) #Removes a specific suffix (from the end of the string) if it exists.