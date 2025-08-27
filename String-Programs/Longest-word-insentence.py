sentence = input("Enter the sentence: ").split()
longest_word = ""

for word in sentence:
    if len(word) > len(longest_word):
        longest_word = word

print("The longest word is:", longest_word)