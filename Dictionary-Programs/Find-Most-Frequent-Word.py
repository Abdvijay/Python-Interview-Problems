# Find the most frequent word in a string

# Input: "apple banana apple orange banana apple"
# Output: "apple"

string = input("Enter the string : ").split()
result = {}
for word in string:
    if word not in result:
        result[word] = 1
    else:
        result[word] = result[word] + 1
maximum = 0
for keys,values in result.items():
    if values > maximum:
        maximum = values
for keys,values in result.items():
    if maximum == values:
        print(keys)