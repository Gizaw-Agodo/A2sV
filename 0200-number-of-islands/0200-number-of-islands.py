class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isBounded(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        
        visited = set()
        
        def dfs (row, col):
            visited.add((row,col))
            for i, j in directions :
                nrow = row + i
                ncol = col + j
                if (nrow,ncol) not in visited:
                    if isBounded(nrow, ncol) and grid[nrow][ncol] == "1":
                        dfs(nrow, ncol)
        
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    island_count += 1
                    
        return island_count