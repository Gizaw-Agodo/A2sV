class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        initialAnd = nums[0]
        
        for i in range(len(nums)):
            initialAnd &= nums[i]
        
        if initialAnd > 0 :
            return 1
        
        i = 0
        count = 0
        currAnd = nums[0]
        
        while i < len(nums):
            currAnd &= nums[i]
            i += 1
            if currAnd == 0:
                count += 1
                if i < len(nums):
                    currAnd = nums[i]
        
        return count
