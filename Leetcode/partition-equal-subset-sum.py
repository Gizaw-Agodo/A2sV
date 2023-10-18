class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        @cache
        def dp(currSum, index):
            if currSum == 0:
                return True
            if  index == len(nums) or currSum < 0:
                return False
            
            return dp(currSum - nums[index], index + 1) or dp(currSum , index + 1)
        

        if sum(nums)%2:
            return False
        return dp(sum(nums)//2 , 0)
        
