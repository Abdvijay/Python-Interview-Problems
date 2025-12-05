# Input: "aaabbc" 

# Output: Possible rearrangement: "ababac"

word = input("Enter the word : ")
dic = {}
for i in word:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
        
sorted_dic = dict(sorted(dic.items(),key=lambda x:x[1],reverse=True))
result = []
count = 0
temp = []
possible = True
final = []
while True:
    for key,value in sorted_dic.items():
        if sorted_dic[key] != -1:
            temp.append(key)
            count += 1
            sorted_dic[key] -= 1

        if sorted_dic[key] == 0:
            sorted_dic[key] = -1

        if count == 2:
            added_combo = "".join(temp)
            result.append(added_combo)
            temp = []
            count = 0
            break
    
    if all(val == -1 for val in sorted_dic.values()):
        if len(temp) != 0:
            result.append(temp[0])
        break
    else:
        continue

final = "".join(result)
if final[-2] == final[-1]:
    possible = False

if possible:
    print(f'Possible Rearrangement is {final}')
else:
    print(f'Rearrangement is impossible')

# Enter the word : aaabbc
# Possible Rearrangement is ababac

# Enter the word : aabb
# Possible Rearrangement is abab

# Enter the word : aaabc
# Possible Rearrangement is abaca

# Enter the word : aaabb
# Possible Rearrangement is ababa

# Enter the word : aabbc
# Possible Rearrangement is ababc

# Enter the word : aaabcdd
# Possible Rearrangement is adadabc

# Enter the word : aaaaaac
# Rearrangement is impossible