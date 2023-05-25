class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
            
        nums.sort()
        start = 3
        end = len(nums)-1
        
        minimum = float('inf')
        for i in range(4):
            diff = nums[end] - nums[start]
            minimum = min(diff, minimum)
            start -= 1
            end -= 1
        return minimum
            
                        
        
            
        
        