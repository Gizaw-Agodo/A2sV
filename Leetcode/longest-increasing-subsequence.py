class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        @cache
        def recursion(index):
           
            maxValue = 1
            for i in range(index + 1, len(nums)):
                if nums[i] > nums[index]:
                    maxValue = max(maxValue,1 + recursion(i))
            return maxValue
        
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, recursion(i))
        return ans
