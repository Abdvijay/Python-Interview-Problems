# Sample Input
# Enter the list elements : 1 2 3 4 5 1 2 3 2 1 3

# Sample Output
# The most frequent elements are [1, 2, 3] which is 3 times repeated

lst = list(map(int,input("Enter the list elements : ").split()))
dic = {}
for i in lst:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
max_value = max([i for i in dic.values()])
result = []
for key,value in dic.items():
    if max_value == value:
        result.append(key)
print(f"The most frequent elements are {result} which is {max_value} times repeated")