class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def isBounded(row, col, n, m):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])
                
        def isBorder(row, col, n, m):
            return row == 0 or col == 0 or row == n - 1 or col == m - 1
            
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        queue = deque([[entrance[0], entrance[1],0]])
        visited = set([(entrance[0], entrance[1])])
        
        def bfs(n, m):
            while queue:
                r,c,d = queue.popleft()
                if isBorder(r, c, n, m) and [r,c] != entrance:
                    return d
                for row , col in directions :
                    nrow , ncol = row + r , col + c
                    if (nrow,ncol) not in visited:
                        if isBounded(nrow, ncol, n ,m) and maze[nrow][ncol] != '+':
                            queue.append([nrow,ncol, d + 1])
                            
                            visited.add((nrow, ncol))
                            
            return -1
                    
        return bfs(len(maze), len(maze[0]))
                    
            