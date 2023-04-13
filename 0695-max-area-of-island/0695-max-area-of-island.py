class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1,0),(0,-1),(0,1),(1,0)]
        visited = set()
        max_area = 0
        
        def dfs(graph, row, col):
            visited.add((row,col))
            area = 1
            for i,j in directions :
                new_row = row + i 
                new_col = col + j
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    if (new_row,new_col) not in visited and grid[new_row][new_col] == 1:
                        area += dfs(graph, new_row, new_col)
            return area
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1 and grid[i][j] not in visited:
                    temp_area = dfs(grid, i, j)
                    max_area = max(temp_area, max_area)
                    
        return max_area
                
                
            