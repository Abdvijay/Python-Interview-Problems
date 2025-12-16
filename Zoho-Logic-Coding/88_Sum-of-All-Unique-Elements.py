lst = list(map(int,input("Enter the list elements : ").split()))
result = []
for i in range(len(lst)):
    flag = True
    for j in range(len(lst)):
        if lst[i] == lst[j] and i != j:
            flag = False
    if flag:
        result.append(lst[i])
print(f"Unique Elements is {result} and Sum of Unique Element is {sum(result)}")

# Sample Input and Sample Output

# Enter the list elements : 1 2 2 3 
# Unique Elements is [1, 3] and Sum of Unique Element is 4

# Enter the list elements : 5 5 5  
# Unique Elements is [] and Sum of Unique Element is 0 # pyright: ignore[reportUndefinedVariable]

# Enter the list elements : 10 20 30
# Unique Elements is [10, 20, 30] and Sum of Unique Element is 60

# Enter the list elements : 4 6 4 7
# Unique Elements is [6, 7] and Sum of Unique Element is 13

# Enter the list elements : 1
# Unique Elements is [1] and Sum of Unique Element is 1