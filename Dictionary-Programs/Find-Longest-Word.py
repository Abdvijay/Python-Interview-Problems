# Find the longest word(s) in a sentence using dictionary

# Input: "I love programming in python"
# Output: {'programming':11}

sentence = input("Enter the sentence : ").split()
dic = {}
for word in sentence:
    dic[word] = len(word)
max_len = max(dic.values())
longest_word = {word : length for word,length in dic.items() if length == max_len}
print(longest_word)