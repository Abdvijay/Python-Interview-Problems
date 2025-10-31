def numIsland(grid):
    if not grid:
        return 0
    
    rows, columns = len(grid), len(grid[0])
    visited = set()
    island = 0

    def dfs(row,column):
        if(row < 0 or row >= rows or column < 0 or column >= columns or grid[row][column] == "0" or (row,column) in visited):
            return
        visited.add((row,column))
        dfs(row + 1,column)
        dfs(row - 1,column)
        dfs(row,column + 1)
        dfs(row,column - 1)

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == "1" and (i,j) not in visited:
                dfs(i,j)
                island += 1
    return island

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

print(numIsland(grid))