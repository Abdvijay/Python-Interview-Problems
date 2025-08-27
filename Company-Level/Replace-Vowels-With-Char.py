# Replace Vowels with ‘*’ in a String

# Input: "Interview"

# Output: "*nt*rv**w"

word = input("Enter the word : ")
ch = input("Enter the character : ")
result = []
for chr in word:
    if chr in 'aeiouAEIOU':
        result.append(ch)
    else:
        result.append(chr)
print(''.join(result))