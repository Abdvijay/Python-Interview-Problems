# Sample Input
# Enter the sentence : i love programming in python

# Sample Output
# i love programming in python in this sentence the longest word is programming

sentence = input("Enter the sentence : ").split()
longest_word = ""
for word in sentence:
    if len(longest_word) < len(word):
        longest_word = word
print(f"{' '.join(sentence)} in this sentence the longest word is {longest_word}")