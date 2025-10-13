# Sample Input
# Enter the list elements : 1 2 3 4 5 6 7 8 9
# Enter the target value : 5

# Sample Output
# [(1, 4), (2, 3)]

lst = list(map(int,input("Enter the list elements : ").split()))
pairs = []
target = int(input("Enter the target value : "))
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] + lst[j] == target:
            pairs.append((lst[i],lst[j]))
print(pairs)