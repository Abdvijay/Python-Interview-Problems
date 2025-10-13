# Sample Input
# Enter the string to count vowels and consonants : vijay

# Sample Output
# The string contains 2 vowels and 3 consonants

string = input("Enter the string to count vowels and consonants : ")
vowels = 0
consonants = 0
for i in string:
    if i.isalpha():
        if i in 'aeiouAEIOU':
            vowels += 1
        else:
            consonants += 1
print(f"The string contains {vowels} vowels and {consonants} consonants")