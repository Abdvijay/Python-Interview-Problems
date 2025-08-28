# Reverse words in a sentence

# Input: "I love coding"
# Output: "coding love I"

sentence = list(input("Enter the sentence : ").split())
print(' '.join(sentence[::-1]))