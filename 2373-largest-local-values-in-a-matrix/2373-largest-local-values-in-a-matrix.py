class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0]*(n-2) for _ in range(n-2)]
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                upper_row_max = max(grid[i][j],grid[i][j+1],grid[i][j+2],grid[i+1][j+1])
                lower_row_max = max(grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2],grid[i+1][j+1])
                left_col_max = max(grid[i][j],grid[i+1][j],grid[i+2][j],grid[i+1][j+1])
                right_col_max = max(grid[i][j+2],grid[i+1][j+2],grid[i+2][j+2],grid[i+1][j+1])
                
                maxLocal[i][j] = max(upper_row_max,lower_row_max,left_col_max,right_col_max)
        return maxLocal  