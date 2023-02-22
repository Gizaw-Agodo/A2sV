class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for end in range(k,len(nums)):
            window_sum += nums[end]
            window_sum -= nums[end-k]
            max_sum = max(max_sum ,window_sum)
        
        return max_sum/k