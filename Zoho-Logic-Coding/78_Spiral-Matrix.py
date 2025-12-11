# Sample Input

# 3 3
# 1 2 3
# 4 5 6
# 7 8 9


# Sample Output

# 1 2 3 6 9 8 7 4 5

rows, cols = map(int, input("Enter rows and cols: ").split())

# Read matrix
matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

top, bottom = 0, rows - 1
left, right = 0, cols - 1

result = []

while top <= bottom and left <= right:

    # 1️⃣ Traverse → (top row)
    for i in range(left, right + 1):
        result.append(matrix[top][i])
    top += 1

    # 2️⃣ Traverse ↓ (right column)
    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1

    # 3️⃣ Traverse ← (bottom row)
    if top <= bottom:
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

    # 4️⃣ Traverse ↑ (left column)
    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print(*result)