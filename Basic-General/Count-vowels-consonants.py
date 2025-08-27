str = input("Enter the string : ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
vowels_count = 0
consonant_count = 0
for i in str:
    if i.isalpha():
        if i in vowels:
            vowels_count += 1
        else:
            consonant_count += 1
print(f'Given String : {str}')
print(f'Vowels Count : {vowels_count}')
print(f'Consonant Count : {consonant_count}')