word = input("Enter the word : ")
result = {}
for i in word:
    if i not in result:
        result[i] = 1
    else:
        result[i] += 1
print(result)