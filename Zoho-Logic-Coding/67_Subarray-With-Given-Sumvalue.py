# Input:
# List: [1, 4, 20, 3, 10, 5]
# Sum: 33

# Output:
# Subarray found: [20, 3, 10]

from itertools import combinations
lst = list(map(int,input("Enter the list elements : ").split()))
target_value = int(input("Enter the target value : "))

combos = []
result = []
for i in range(2,len(lst)+1):
    temp = combinations(lst,r=i)
    for comb in temp:
        sort_combo = sorted(comb)
        combos.append(comb)
for combo in combos:
    sum_value = sum(combo)
    if sum_value == target_value:
        result.append(combo)
print(f"Sub Array found : {result}")

# Sample Input
# Enter the list elements : 1 4 20 3 10 5
# Enter the target value : 33

# Sample Output
# Sub Array found : [(20, 3, 10), (1, 4, 20, 3, 5)]