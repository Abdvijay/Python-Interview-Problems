sentence = input("Enter the sentence : ")
dic = {"a":0,"e":0,"i":0,"o":0,"u":0}
for ch in sentence:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            dic[ch.lower()] += 1
print(dic)

# Sample Input and Sample Output

# Enter the sentence : hellow
# {'a': 0, 'e': 1, 'i': 0, 'o': 1, 'u': 0}

# Enter the sentence : education
# {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

# Enter the sentence : PYTHON
# {'a': 0, 'e': 0, 'i': 0, 'o': 1, 'u': 0}

# Enter the sentence : why
# {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Enter the sentence : this is a test
# {'a': 1, 'e': 1, 'i': 2, 'o': 0, 'u': 0}