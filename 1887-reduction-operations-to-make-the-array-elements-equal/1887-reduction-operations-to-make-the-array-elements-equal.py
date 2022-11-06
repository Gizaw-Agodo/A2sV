class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        step = 0
        maximum = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] != nums[i]:
                step +=1
            maximum +=step
        return maximum
        