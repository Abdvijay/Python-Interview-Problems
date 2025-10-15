# Sample Input
# Enter the list elements : 1 2 3 4 5 6 7
# Before Reverse List : [1, 2, 3, 4, 5, 6, 7]

# Sample Output
# After  Reverse List : [7, 6, 5, 4, 3, 2, 1]

lst = list(map(int,input("Enter the list elements : ").split()))
mid = len(lst) // 2
l = len(lst)
count = 0
print(f"Before Reverse List : {lst}")
for i in range(l):
    temp = lst[i]
    lst[i] = lst[l-i-1]
    lst[l-i-1] = temp
    count += 1
    if count == mid:
        break
print(f'After  Reverse List : {lst}')