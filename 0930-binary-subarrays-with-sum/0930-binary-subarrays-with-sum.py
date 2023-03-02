class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = defaultdict(int)
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum == goal : 
                count += 1
            if prefix_sum - goal in dic:
                count += dic[prefix_sum-goal]
            dic[prefix_sum] += 1
            
        return count
            