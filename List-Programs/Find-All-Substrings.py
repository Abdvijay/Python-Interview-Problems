# Find all substrings of a string

# Input: "abc"
# Output: ['a','b','c','ab','bc','abc']

string = input("Enter the string : ")
result = []
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        result.append(string[i:j])
result.sort(key=lambda x:(len(x),x))
print(result)