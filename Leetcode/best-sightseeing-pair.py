class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [0]*len(values)
        dp[1] = values[1] + values[0] - 1
        answer = dp[1]

        for i in range(2,len(values)):
            value1 = dp[i-1] - values[i-1] + values[i] - 1
            value2 = values[i] + values[i-1] - 1
            dp[i] = max(value1, value2)
            answer = max(answer, dp[i])

        return answer