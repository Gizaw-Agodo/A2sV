class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        val =  nums[-1] - nums[0] - 2*k
        if val < 0:
            return 0
        return val
        
