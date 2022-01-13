class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left, right = 0, 0
        counter = 0
        max_num = nums[left]
        min_num = nums[left]
        while right < len(nums):
            min_num = min(nums[right], min_num)
            max_num = max(nums[right], max_num)
            if abs(max_num-min_num) <= limit: 
                counter = max(counter, right-left+1)
            if abs(max_num-min_num) > limit:
                left += 1
                if right < len(nums):
                    max_num = max(nums[left:right+1])
                    min_num = min(nums[left:right+1])
            right += 1
        return counter
