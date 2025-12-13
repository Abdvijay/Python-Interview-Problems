lst = list(map(int,input("Enter the list elements : ").split()))
pos = [i for i in lst if i >= 0]
neg = [i for i in lst if i < 0]

result = []

# i = 0
# # while i < len(pos) or i < len(neg):
# #     if len(pos) == 0:
# #         pass
# #     else:
# #         result.append(pos[0])
# #         pos.remove(pos[0])
# #     i += 1
# #     if len(neg) == 0:
# #         pass
# #     else:
# #         result.append(neg[0])
# #         neg.remove(neg[0])

i = j = 0

while i < len(pos) or j < len(neg):
    if i < len(pos):
        result.append(pos[i])
        i += 1
    if j < len(neg):
        result.append(neg[j])
        j += 1

print(f'Alternates : {result}')

# Sample Input and Sample Output

# Enter the list elements : 1 -2 3 -4 5 -6
# Alternates : [1, -2, 3, -4, 5, -6]

# Enter the list elements : -1 2 -3 4 -5 6
# Alternates : [2, -1, 4, -3, 6, -5]

# Enter the list elements : 5 -1 -2 3 -4
# Alternates : [5, -1, 3, -2, -4]

# Enter the list elements : 5 2 4 5 -1   
# Alternates : [5, -1, 2, 4, 5]

# Enter the list elements : -4 -2 4 5 6
# Alternates : [4, -4, 5, -2, 6]