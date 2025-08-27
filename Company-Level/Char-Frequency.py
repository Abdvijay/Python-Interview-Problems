# Print Characters with Frequency in Order

# Input: "success"

# Output: s=3, u=1, c=2, e=1

word = input("Enter the word : ")
freq = {}
for chr in word:
    if chr in freq:
        freq[chr] += 1
    else:
        freq[chr] = 1
print(', '.join(f'{key}={value}'for key,value in freq.items()))