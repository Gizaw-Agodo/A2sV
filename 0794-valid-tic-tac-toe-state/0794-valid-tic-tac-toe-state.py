class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
         #Check the rows
        x_win = False
        o_win = False
        
        # check if x_wins
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == "X":
                   x_win = True
            elif board[0][i] == board[1][i] == board[2][i] == "X":
                   x_win = True
										
            elif board[0][0] == board[1][1] == board[2][2]  == "X":
                    x_win = True
                    
            elif  board[0][2] == board[1][1] == board[2][0] == "X":
                   x_win = True
                   
        # check if 0_wins     
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == "O":
                   o_win = True
            elif board[0][i] == board[1][i] == board[2][i] == "O":
                   o_win = True						
            elif board[0][0] == board[1][1] == board[2][2]  == "O":
                    o_win = True
            elif board[0][2] == board[1][1] == board[2][0] == "O":
                   o_win = True
            
						
    
        x_count = 0
        o_count = 0
        
        for i in range (len(board)):
            element = list(board[i])
            
            for character in element:
                if  character == "X":
                    x_count+=1
                if character == "O":
                    o_count +=1
        
        
        if o_count > x_count or x_count-o_count>1:
            return False
        
        if o_win:
            if x_win:
                return False
            return o_count == x_count
        
        if x_win and x_count!=o_count+1:
            return False

        return True
        