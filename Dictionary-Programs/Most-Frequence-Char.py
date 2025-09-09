# Find most frequent character in a string

# Input: "mississippi"
# Output: 'i' (appears 4 times)

word = input("Enter the word : ")
result = {}
for ch in word:
    if ch not in result:
        result[ch] = 1
    else:
        result[ch] = result[ch] + 1
maximum = 0
for values in result.values():
    if values > maximum:
        maximum = values
for keys,values in result.items():
    if values == maximum:
        print(keys)
        break