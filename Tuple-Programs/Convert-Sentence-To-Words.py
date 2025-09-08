# Convert sentence into tuple of words

# Input: "Python is fun"
# Output: ("Python", "is", "fun")

sentence = input("Enter the sentence : ").split()
words = []
for word in sentence:
    words.append(word)
print(tuple(words))