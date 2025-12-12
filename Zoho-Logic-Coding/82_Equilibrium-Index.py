lst = list(map(int,input("Enter the list elements : ").split()))
equilibrium_index = 0
flag = False
for i in range(len(lst)):
    left_sum = 0
    right_sum = 0
    
    for j in range(i):
        left_sum += lst[j]
    
    for k in range(i+1,len(lst)):
        right_sum += lst[k]
    
    if left_sum == right_sum:
        equilibrium_index = i
        flag = True
        break
if flag:
    print(f'Equilibrium index of {lst} is {equilibrium_index}')
else:
    print(f'There is no Equilibrium Index')