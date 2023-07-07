class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*n
        dp[-1] = questions[-1][0]
        for i in range(n - 2, -1, -1):
            point, jump = questions[i]
            nextIndex = i + jump + 1
            nextPoint = 0 if nextIndex >= n else dp[nextIndex]
            dp[i] = max(dp[i+1], point + nextPoint )
        return dp[0]

