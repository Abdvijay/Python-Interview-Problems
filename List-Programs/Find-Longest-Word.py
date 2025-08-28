# Find longest word in a sentence

# Input: "The quick brown fox jumps"
# Output: "jumps"

sentence = input("Enter the sentence : ").split()
dic = {}
for word in sentence:
    count = 0
    for ch in word:
        count += 1
    dic[count] = word
maximum = max(dic)
print("The longest word is : ",dic[maximum])