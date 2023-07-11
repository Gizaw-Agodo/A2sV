class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(index, cur_sum):
            if index == len(nums):
                if cur_sum == target:
                    return 1
                else:
                    return 0
            
            key = (index, cur_sum)
            if key in memo:
                return memo[key]
            
            pos_value = dp(index + 1 ,  cur_sum + nums[index])
            neg_value = dp(index + 1 , cur_sum - nums[index])

            memo[key] = pos_value + neg_value
            return memo[key]
        
        return dp(0, 0)

    