class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            temp = [board[i][j] for j in range(9) if board[i][j].isdigit()]
            if len(temp)!= len(set(temp)):
                return False
        
        for i in range(9):
            temp = [board[j][i] for j in range(9) if board[j][i].isdigit()]
            if len(temp)!= len(set(temp)):
                return False
        
        move_list = [[1,1],[-1,-1],[1,0],[0,1],[-1,1],[1,-1],[-1,0],[0,-1],[0,0]]
        for i in range(1,9,3):
            for j in range(1,9,3):
                temp = [board[i+k][j+l] for k,l in move_list if board[i+k][j+l].isdigit()]
                if len(temp)!= len(set(temp)):
                    return False
        return True
                
        
        