# Sample Output for nested loop

# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]

# Sample Output for list comprehension

# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]

result = []
for i in range(1,3):
    for j in range(1,4):
        result.append((i,j))
print(result)

lst_com = [(i,j) for i in range(1,3) for j in range(1,4)]
print(lst_com)