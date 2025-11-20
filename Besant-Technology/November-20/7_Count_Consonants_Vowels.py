word = input("Enter the string : ").lower()
vowels = 0
consonants = 0
for i in word:
    if i.isalpha():
        if i in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print(f'The given string is {word} and it has {vowels} vowels and {consonants} consonants')

# OUTPUT

# Enter the string : vijay
# The given string is vijay and it has 2 vowels and 3 consonants

# Enter the string : 2234VIJAY
# The given string is 2234vijay and it has 2 vowels and 3 consonants