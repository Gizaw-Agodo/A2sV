class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        dp[0] = matrix[0]

        for row in range(1, n):
            for col in range(n):
                if col == 0:
                    minimum = min(dp[row-1][col], dp[row-1][col+1])
                    dp[row][col] = matrix[row][col] + minimum
                elif col == n-1:
                    minimum = min(dp[row-1][col-1], dp[row-1][col])
                    dp[row][col] = matrix[row][col] + minimum
                else:
                    minimum = min(dp[row-1][col-1], dp[row-1][col], dp[row-1][col+1])
                    dp[row][col] = matrix[row][col] + minimum
        
        min_sum = min(dp[n-1])
        return min_sum

       