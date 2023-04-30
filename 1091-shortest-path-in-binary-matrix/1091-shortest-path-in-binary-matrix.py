class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # time O(M * N)
        # space O(M * N)
        
        n = len(grid)
        
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        
        def isBounded (row, col, n):
            return 0 <= row < n and 0 <= col < n
        
        # check for 1 at start and end 
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        queue = deque([(0, 0, 1)])
        
        def bfs ():
            
            while queue:
                r, c, d = queue.popleft()
                if r == n-1 and c == n-1 :
                    return d
                for row, col in directions :
                    nrow, ncol = r + row, col + c
                    if isBounded(nrow, ncol, n) and not grid[nrow][ncol]:
                        queue.append((nrow, ncol, d + 1))
                        grid[nrow][ncol] = 1
            return -1
        return bfs()
