class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0 
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0]*n for _ in range(m)]
        
        dp[m-1][n-1] = 1
        
        for i in range(m-1 , -1, -1):
            for j in range(n-1, -1 , -1):
                
                value = 0
        
                if j + 1 < n and obstacleGrid[i][j + 1] != 1:
                    value += dp[i][j + 1] 
                if i + 1 < m and obstacleGrid[i + 1][j] != 1 :
                    value += dp[i + 1][j]
                    
                dp[i][j] += value
                
        return dp[0][0]
            
                