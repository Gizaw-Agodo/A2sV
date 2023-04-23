class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        directions = [(-1,0),(0,-1),(1,0),(0,1),(1,1),(-1,-1),(1,-1),(-1,1)]
        def isBounded(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        visited = set()
        def dfs(row, col):
            
            # check for mine
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return
            
            # check for empty squre 
            if board[row][col] == 'E':
                # get the number of mines 
                count = 0
                for i, j in directions:
                    nrow = row + i
                    ncol = col + j
                    if isBounded(nrow, ncol):
                        if board[nrow][ncol] == 'M' or board[nrow][ncol] == 'X':
                            count += 1

                if count != 0:
                    board[row][col] = str(count)
                    return 

                board[row][col] = 'B'
                visited.add((row, col))

                for i, j in directions:
                    nrow = row + i
                    ncol = col + j
                    if isBounded(nrow, ncol) and (nrow , ncol) not in visited:
                        dfs(nrow, ncol)

                    
        dfs (click[0], click[1])
        return board