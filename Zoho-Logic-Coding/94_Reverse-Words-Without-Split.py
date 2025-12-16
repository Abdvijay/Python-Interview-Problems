sentence = input("Enter the sentence : ")
words = []
current = []
for char in sentence:
    if char == " ":
        if current:
            words.append("".join(current))
            current = []
    else:
        current.append(char)

if current:
    words.append("".join(current))

result = " ".join(reversed(words))
print(f"Original Sentence : {"".join(sentence)}")
print(f"After Reverse     : {result}")

# Sample Input and Sample Output

# Enter the sentence : one two three
# Original Sentence : one two three
# After Reverse     : three two one

# Enter the sentence : sir
# Original Sentence : sir
# After Reverse     : sir

# Enter the sentence : 1 2 3
# Original Sentence : 1 2 3
# After Reverse     : 3 2 1

# Enter the sentence : python is fun and
# Original Sentence : python is fun and
# After Reverse     : and fun is python