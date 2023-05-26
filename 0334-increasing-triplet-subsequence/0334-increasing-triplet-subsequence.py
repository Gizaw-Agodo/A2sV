class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = float('inf')
        second_min = float('inf')
                
        for i in range(len(nums)):
            if second_min < nums[i]:
                return True
            if nums[i] > first_min:
                second_min = min(second_min, nums[i])
            
            first_min = min(first_min, nums[i])
        
        return False
            
        