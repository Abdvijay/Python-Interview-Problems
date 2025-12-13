lst = list(map(int,input("Enter the list elements : ").split()))
rev = sorted(list(set(lst)))
result = []

for i in lst:
    ind = rev.index(i)
    result.append(ind+1)
print(result)

# Sample Input and Sample Output

# Enter the list elements : 40 10 20 30
# [4, 1, 2, 3]

# Enter the list elements : 100 100 50 
# [2, 2, 1]

# Enter the list elements : 5    
# [1]

# Enter the list elements : 1 2 3  
# [1, 2, 3]

# Enter the list elements : 8 6 7 6
# [3, 1, 2, 1]