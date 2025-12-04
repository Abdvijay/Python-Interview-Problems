# Sample example 

# Input:
# [10, 22, 9, 33, 21, 50, 41, 60]

# Output:
# LIS: [10, 22, 33, 50, 60]
# Length: 5


lst = list(map(int,input("Enter the list elements : ").split()))
end_lst = {}
for i in range(len(lst)):
    sub_lst = []
    cmp = lst[i]
    sub_lst.append(cmp)
    for j in range(i+1,len(lst)):
        if cmp < lst[j]:
            cmp = lst[j]
            sub_lst.append(cmp)
    key = len(sub_lst)
    if key in end_lst:
        end_lst[key].append(sub_lst)
    else:
        end_lst[key] = [sub_lst]
maximum = max(end_lst.keys())
print(f"LIS : {end_lst[maximum][0]}")
print(f'Length : {maximum}')