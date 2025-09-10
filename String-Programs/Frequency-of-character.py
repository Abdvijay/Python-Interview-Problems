# Enter the string : mississippi
# {'m': 1, 'i': 4, 's': 4, 'p': 2}

word = input("Enter the string : ")
dict = {}
for i in word:
    if i in dict:
        dict[i] += 1 
    else:
        dict[i] = 1
print(dict)