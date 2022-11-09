class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(1,len(nums)-1):
            if nums[i]> nums[0] and nums[i]< nums[-1]:
                count +=1
        return count 
        