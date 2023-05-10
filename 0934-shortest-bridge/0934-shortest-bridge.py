class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def isBounded (row, col, n):
            return 0 <= row < n and 0 <= col < n
        
        queue = deque([])
        queue2 = deque([])
        visited = set()
        visited2 = set()
        
        for i in range(n):
            flag = False
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    visited.add((i,j))
                    queue2.append((i,j,0))
                    visited2.add((i,j))
                    flag = True
                    break
            if flag:
                break
        
        def bfs1():
            while queue:
                r, c = queue.popleft()
                for row, col in directions :
                    nrow, ncol = r + row, col + c
                    
                    if isBounded(nrow, ncol, n) and grid[nrow][ncol]:
                        if (nrow, ncol) not in visited:
                            queue.append((nrow, ncol))
                            queue2.append((nrow,ncol,0))
                            visited.add((nrow,ncol))
                            visited2.add((nrow,ncol))
        bfs1()
        
        def bfs2 ():
            
            while queue2:
                
                r, c, d = queue2.popleft()
                
                for row, col in directions :
                    nrow, ncol = r + row, col + c
                    
                    if isBounded(nrow, ncol, n) and (nrow,ncol) not in visited2:
                        print(nrow, ncol)
                        if grid[nrow][ncol] == 1:
                            return d 
                        queue2.append((nrow, ncol, d + 1))
                        visited2.add((nrow,ncol))
       
        return bfs2()       
