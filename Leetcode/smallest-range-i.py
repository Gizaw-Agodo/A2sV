class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        val =  nums[-1] - nums[0] - 2*k
        return max(0,val)
        
