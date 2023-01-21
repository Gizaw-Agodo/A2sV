class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        answer  = []
        for i in range(len(nums)):
            if nums[i] == target:
                answer.append(i)
        return answer
