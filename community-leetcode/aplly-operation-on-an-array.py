class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
        start = 0
        for i in range(n):
            if nums[i]!=0:
                nums[i],nums[start] = nums[start],nums[i]
                start +=1
            
        return nums
