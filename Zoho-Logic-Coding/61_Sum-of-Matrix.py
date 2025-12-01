m = int(input("Enter the m value : "))
n = int(input("Enter the n value : "))
print("Enter the matrix values : ")
matrix = []
result_sum = 0
for i in range(m):
    sub_list = []
    for j in range(n):
        value = int(input())
        sub_list.append(value)
        result_sum += value
    matrix.append(sub_list)
print(f'The sum of result of {matrix} is {result_sum}')

# Sample Input and Sample Output :

# Enter the m value : 3
# Enter the n value : 3
# Enter the matrix values : 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# The sum of result of [[1, 2, 3], [4, 5, 6], [7, 8, 9]] is 45