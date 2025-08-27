lst = list(map(int,input("Enter the list elements : ").split()))
N = int(input("Enter the N : "))
result = []
count = 1
sub_list = []
for i in lst:
    if count <= N:
        sub_list.append(i)
        count += 1
    if count == N+1:
        count = 1
        result.append(sub_list)
        sub_list = []
if sub_list:
    result.append(sub_list)
print(result)