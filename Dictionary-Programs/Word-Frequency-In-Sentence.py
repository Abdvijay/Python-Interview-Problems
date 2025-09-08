# Word frequency in a sentence

# Input: "I love coding and I love Python"
# Output: {'I':2, 'love':2, 'coding':1, 'and':1, 'Python':1}

sentence = input("Enter the sentence : ").split()
dic = {}
for word in sentence:
    if word in dic:
        dic[word] = dic[word] + 1
    else:
        dic[word] = 1
print(dic)