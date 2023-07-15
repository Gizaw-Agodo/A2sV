class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if len(nums) <= 2 : return len(nums)
        longest = 2
        dp = [defaultdict(int) for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[j] - nums[i]
                if dp[j][diff]:
                    dp[i][diff] = dp[j][diff] + 1
                else: 
                    dp[i][diff] = 2
                longest = max(longest, dp[i][diff])
                
        return longest
        
