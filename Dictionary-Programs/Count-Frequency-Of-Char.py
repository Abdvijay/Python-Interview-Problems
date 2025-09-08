# Count frequency of each character (ignoring spaces & case)

# Input: "Hello World"
# Output: {'h':1, 'e':1, 'l':3, 'o':2, 'w':1, 'r':1, 'd':1}

from collections import Counter
sentence = input("Enter the sentence : ").lower()
# dic = {}
# for ch in sentence:
#     if ch != " ":
#         if ch not in dic:
#             dic[ch] = 1
#         else:
#             dic[ch] = dic[ch] + 1
# print(dic)

result = Counter(ch for ch in sentence if ch != " ")
print(dict(result))