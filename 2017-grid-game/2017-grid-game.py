class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        
        #finding the prefix sum
        for i in range(1,length):
            grid[0][i] += grid[0][i-1]
            grid[1][i] += grid[1][i-1]
        
        # adding buffer zero
        grid[1] = [0] + grid[1]

        #player2 score is the min of the max of score from row 1 and 2
        max_player2_score = float("inf")
        for i in range(length):
            row1_score = grid[0][length-1] - grid[0][i]
            row2_score = grid[1][i]
            
            #player_2 maximize its score
            p2Score = max(row1_score,row2_score)
            
            #player1 minimize p2 score
            max_player2_score = min(p2Score,max_player2_score)
        
        return max_player2_score
        