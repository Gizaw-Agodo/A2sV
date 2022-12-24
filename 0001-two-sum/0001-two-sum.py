class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            d=target-nums[i]
            if d in nums[i+1::]:
                return [i,nums.index(d,i+1,len(nums))]
