# Group elements of list by first element of tuple

# Input: [('a',1), ('b',2), ('a',3), ('b',4)]
# Output: {'a':[1,3], 'b':[2,4]}

# import ast
# tuples = ast.literal_eval(input("Enter the tuples of elements : "))
# dic = {}
# key = []
# for tup in tuples:
#     if tup[0] not in key:
#         key.append(tup[0])
# for i in range(len(key)):
#     value = []
#     for tup in tuples:
#         if key[i] == tup[0]:
#             value.append(tup[1])
#     dic[key[i]] = value
# print(dic)

import ast
tuples = ast.literal_eval(input("Enter the tuples of elements : "))
dic = {}
for key,value in tuples:
    if key not in dic:
        dic[key] = []
    dic[key].append(value)
print(dic)