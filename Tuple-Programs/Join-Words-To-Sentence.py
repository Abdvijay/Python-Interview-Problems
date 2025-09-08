# Join tuple of words into a sentence

# Input: ("I", "love", "coding")
# Output: "I love coding"

import ast
tuples = ast.literal_eval(input("Enter the tuples : "))
sentence = []
for tup in tuples:
    sentence.append(tup)
print(' '.join(sentence))