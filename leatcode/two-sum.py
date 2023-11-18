class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index,  num in enumerate(nums):
            if target - num in seen:
                return [seen[target-num], index ]
            else:
                seen[num] = index
            