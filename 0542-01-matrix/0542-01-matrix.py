class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # time O(M * N) 
        # space O(M * N)
        
        def isBounded(row, col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        # start from 0 cells 
        queue = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = -1
                        
        def bfs():
            while queue:
                i,j = queue.popleft()
                for row, col in directions : 
                    nrow = row + i 
                    ncol = col + j
                    if isBounded(nrow, ncol) and mat[nrow][ncol] == -1:
                        mat[nrow][ncol] = mat[i][j] + 1
                        queue.append((nrow, ncol))
        bfs()
        return mat
                            
                            
                