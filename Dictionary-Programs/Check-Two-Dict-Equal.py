# Check if two dictionaries are equal

# Input: {'a':1, 'b':2}, {'b':2, 'a':1}
# Output: True

import ast
dic1 = ast.literal_eval(input("Enter the dictionary one : "))
dic2 = ast.literal_eval(input("Enter the dictionary two : "))
flag = False
for keys in dic1.keys():
    if keys in dic2:
        if dic1[keys] == dic2[keys]:
            flag = True
        else:
            flag = False
if flag:
    print(flag)
# print(dic1 == dic2)