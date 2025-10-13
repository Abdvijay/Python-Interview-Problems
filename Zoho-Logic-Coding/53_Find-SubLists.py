# Sample Input
# Enter the list elements : 1 2 3

# Sample Output
# [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

from itertools import combinations

lst = list(map(int, input("Enter the list elements : ").split()))
combo = [combinations(lst, r) for r in range(1, len(lst) + 1)]  # square brackets

res = [list(sublist) for group in combo for sublist in group]
print(res)