class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        for i in range(1,len(nums)):
            nums[i] +=nums[i-1]
        for i in range(len(nums)-1):
            if nums[i] >= nums[-1]-nums[i]:
                count +=1
        return count