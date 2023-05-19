class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m,n = len(grid), len(grid[0])
        
        def isBounded(x,y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        streets = {
                   1: [(0,1), (0,-1)],
                   2: [(1,0), (-1,0)],
                   3: [(0,-1), (1,0)],
                   4: [(0,1), (1,0)],
                   5: [(0,-1), (-1,0)],
                   6: [(-1,0), (0,1)]
                  }
        
        visited = set((0,0))
        
        def dfs(i,j):
            
            if [i,j] == [m-1,n-1]:
                return True
            
            
            for row,col in streets[grid[i][j]]:
                nrow, ncol = i+row, j+col
                if isBounded(nrow,ncol) and (nrow,ncol) not in visited:
                    visited.add((nrow,ncol))
                    if (-1*row,-1*col) in streets[grid[nrow][ncol]]:
                        if dfs(nrow, ncol):
                            return True
            
            return False
        
        return dfs(0,0)
                    
            
    