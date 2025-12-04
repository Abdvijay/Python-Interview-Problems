# Input:
# "aaabbcddd"
# Output:
# "a3b2c1d3"

word = input("Enter the word : ")
dic = {}
result = []
for ch in word:
    if ch not in dic:
        dic[ch] = 1
    else:
        dic[ch] += 1
for key,value in dic.items():
    result.append(key)
    result.append(str(value))
print(f'Result is {"".join(result)}')

# Enter the word : aaabbcddd
# Result is a3b2c1d3