class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # temp = board.copy()
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         board[i][j] = "X"
        # print(temp)
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def isBoundary(row, col):
            if row == 0 or row == len(board)-1 or col == 0 or col == len(board[0])-1:
                return True
        
        def isBounded(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        visited = set()
    
        def dfs(row, col):
            visited.add((row , col))
            for i, j in directions:
                nrow = row + i
                ncol = col + j
                if (nrow,ncol) not in visited:
                    if isBounded(nrow, ncol) and board[nrow][ncol] == "O":
                        dfs(nrow, ncol)
      
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] not in visited and isBoundary(i,j) and board[i][j] == "O":
                    dfs(i,j)
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"
        
        