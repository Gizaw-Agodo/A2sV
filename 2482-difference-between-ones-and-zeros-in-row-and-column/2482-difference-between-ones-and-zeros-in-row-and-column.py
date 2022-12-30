class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_count = [[0,0] for i in range(len(grid))]
        col_count = [[0,0] for _ in range(len(grid[0]))]
        diff = [[0]*len(grid[0])for i in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    row_count[i][1] +=1
                    col_count[j][1] +=1
                elif grid[i][j] == 0:
                    row_count[i][0] +=1
                    col_count[j][0] +=1
        
        
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[i])):
                diff[i][j] = row_count[i][1]+ col_count[j][1] - row_count[i][0]-col_count[j][0]
        return diff
            
