# Enter the sentence by space : hi vijay how are you
# Hi Vijay How Are You

sentence = input("Enter the sentence by space : ").split()
result = []
for word in sentence:
    result.append(word.capitalize())
print(' '.join(result))