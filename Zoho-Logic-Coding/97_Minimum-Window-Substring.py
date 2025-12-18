sentence = input("Enter the sentence : ")
pattern = input("Enter the pattern : ")
temp = []
possible = []
target_dict = {}
result = []

# Setting target dictionary with count values
for i in pattern:
    if i not in target_dict:
        target_dict[i] = 1
    else:
        target_dict[i] += 1

# Finding all possible substrings
for i in range(len(sentence)):
    temp.append(sentence[i])
    for j in range(i+1,len(sentence)):
        temp.append(sentence[j])
        dummy = "".join(temp)
        possible.append(dummy)
    temp = []

# Checking the all target element are inside in the every possible substring
# Check target element count values also
for res in possible:
    if all(values <= res.count(key) for key,values in target_dict.items()):
        flag = True
    else:
        flag = False

    if flag:
        result.append(res)

# Sorting all feasible substring using the len option
result.sort(key=len)
if result:
    print(result[0])
else:
    print(result)

# Sample Input and Sample Output

# Enter the sentence : ADOBECODEBANC
# Enter the pattern : ABC
# BANC

# Enter the sentence : abccdee
# Enter the pattern : cee
# cdee

# Enter the sentence : abcdee
# Enter the pattern : ez
# []