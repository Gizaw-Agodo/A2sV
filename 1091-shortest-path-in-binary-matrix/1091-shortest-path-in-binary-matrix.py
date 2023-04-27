class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        
        visited = set([(0,0)])
        queue = deque([(0,0)])
        
        shortd = [[float('inf') for i in range(m)] for _ in range(n)]
        
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        shortd[0][0] = 1
        
        def isBounded (row, col, grid):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
            
        def bfs(grid):
            distance = 1
            while queue:
               
                length = len(queue)
                
                for i in range(length):
                    
                    i,j = queue.popleft()
                    for row,col in directions : 
                        nrow = row + i
                        ncol = col + j

                        if isBounded(nrow, ncol, grid) and (nrow,ncol) not in visited:
                            if grid[nrow][ncol] == 0:
                                shortd[nrow][ncol] = min(shortd[nrow][ncol],distance + 1)
                                visited.add((nrow, ncol))
                                queue.append((nrow,ncol))

                distance += 1
        bfs(grid)
        
        print(shortd)
        return shortd[m-1][n-1] if shortd[m-1][n-1] != float('inf') else -1
                            