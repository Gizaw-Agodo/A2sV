class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def divisionSum (nums,divisor):
            temp_sum = 0
            for num in nums:
                temp_sum += ceil(num/divisor)
            return temp_sum
        
        left = 1
        right = max(nums) + 1
        while left <= right:
            mid = left + (right-left)//2
            result = divisionSum(nums, mid)
            if result <= threshold:
                right = mid - 1
            elif result > threshold :
                left =  mid + 1
                
        return left
        
        