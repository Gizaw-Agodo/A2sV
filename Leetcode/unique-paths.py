class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1
      
        def answerOrDefault(i, j):
            if 0 <= i < m and 0 <= j < n:
                return dp[i][j]
            return 0
      
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):                
                rightMove = answerOrDefault(row, col + 1)
                downMove = answerOrDefault(row + 1, col)
                dp[row][col] += rightMove + downMove
        
        return dp[0][0]
