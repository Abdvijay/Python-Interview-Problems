n = int(input("Enter the n value : "))
lst = list(map(int,input("Enter the list elements : ").split()))
so_lst = sorted(lst)
result = []
start = so_lst[0]
for i in range(start,n+1):
    if i not in so_lst:
        result.append(i)
print(f'Missing values : {result}')

# OUTPUT

# Enter the n value : 10       
# Enter the list elements : 1 5 4 2 8
# Missing values : [3, 6, 7, 9, 10]