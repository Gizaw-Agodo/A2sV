class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        memo = {}

        def dp (i, j):
            if i >= len(s) or j < 0:
                return 0
            index = (i,j)
            if index in memo:
                return memo[index]

            if s[i] == s[j]:
                memo[index] = 1 + dp(i + 1, j - 1)
                return memo[index]
            
            option1 = dp(i + 1, j)
            option2 = dp(i, j - 1)

            memo[index] =  max(option1, option2)
            return memo[index]
        
        return dp(0, len(s)-1)
