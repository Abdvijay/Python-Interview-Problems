# Sort Words in a Sentence Alphabetically

# Input: "this is a test"

# Output: "a is test this"

sentence = input("Enter the sentence : ")
lst = []
words = []
for chr in sentence:
    if chr == ' ':
        lst.append(''.join(words))
        words = []
    else:
        words.append(chr)
if words:
    lst.append(''.join(words))
lst.sort()
print(' '.join(lst))