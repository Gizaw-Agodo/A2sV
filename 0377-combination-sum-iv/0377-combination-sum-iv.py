class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [0]*(target + 1)
        memo[0] = 1
        
        for i in range(1,target + 1):
            for val in nums:
                if val <= i:
                    memo[i] += memo[i-val]
        return memo[-1]