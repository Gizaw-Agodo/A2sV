class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        visited  = set()
        def dfs(row,col):
            
            if grid1[row][col] == 0:
                return False
            
            visited.add((row,col))                    
            isSub = True

            for i,j in directions:
                nrow = row + i
                ncol = col + j
                if 0 <= nrow < len(grid1) and 0 <= ncol < len(grid1[0]):
                    if grid2[nrow][ncol] == 1 and (nrow, ncol) not in visited:
                          isSub = dfs(nrow, ncol) and isSub
            return isSub
        
        
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i,j) not in visited:
                    count += dfs(i,j)
        return count

        
        