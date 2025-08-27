from itertools import permutations

str = input("Enter the string : ")
result = permutations(str)
lst = []
for i in result:
    lst.append(''.join(i))
print(lst)