sentence = input("Enter the sentence by space : ").split()
result = []
for i in sentence:
    result.append(i.capitalize())
print(' '.join(result))