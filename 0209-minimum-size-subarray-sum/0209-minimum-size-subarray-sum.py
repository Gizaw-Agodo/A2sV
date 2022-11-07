class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minimum = float("inf")
        fast,slow = 0,0
        prefsum = 0
        while fast < n :
            prefsum+=nums[fast]
            while prefsum >= target:
                minimum = min(minimum,fast-slow+1)
                prefsum -= nums[slow]
                slow+=1
            fast+=1
        return minimum if minimum != float("inf") else 0
            

            