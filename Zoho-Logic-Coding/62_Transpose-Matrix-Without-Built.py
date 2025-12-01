rows = int(input("Enter the rows count : "))
columns = int(input("Enter the columns count : "))
print("Enter the matrix values : ")
matrix = []
for i in range(rows):
    sub_list = []
    for j in range(columns):
        value = int(input())
        sub_list.append(value)
    matrix.append(sub_list)

count = 0
transpose_matrix = []
flatten_matrix = [value for rows in matrix for value in rows]
sub_list = []
for i in flatten_matrix:
    sub_list.append(i)
    count += 1
    if count == rows:
        transpose_matrix.append(sub_list)
        sub_list = []
        count = 0
print(f'Original  Matrix is {matrix}')
print(f'Transpose Matrix is {transpose_matrix}')

# Sample Input and Sample Output :

# Enter the rows count : 2
# Enter the columns count : 3
# Enter the matrix values : 
# 1
# 2
# 3
# 4
# 5
# 6
# Original  Matrix is [[1, 2, 3], [4, 5, 6]]
# Transpose Matrix is [[1, 2], [3, 4], [5, 6]]