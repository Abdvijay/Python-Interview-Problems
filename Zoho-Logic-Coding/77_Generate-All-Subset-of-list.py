# from itertools import combinations
# lst = list(map(str,input("Enter the list elements : ").split()))
# n = len(lst)
# for i in range(n+1):
#     result = []
#     result = combinations(lst,r=i)
#     for p in result:
#         print(p)

# SAMPLE INPUT
# Enter the list elements : 1 2 3

# SAMPLE OUTPUT
# ()
# ('1',)
# ('2',)
# ('3',)
# ('1', '2')
# ('1', '3')
# ('2', '3')
# ('1', '2', '3')

lst = list(map(str, input("Enter list elements : ").split()))
n = len(lst)
result = [[]]  # start with empty subset

for elem in lst:
    # For each existing subset, add a new subset including the current element
    new_subsets = []
    for subset in result:
        new_subsets.append(subset + [elem])
    result.extend(new_subsets)

result.sort(key=len)
# Print all subsets
for s in result:
    print(s)