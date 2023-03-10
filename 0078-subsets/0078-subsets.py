class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        def backtrack(index, subset):
            if index >= len(nums):
                return
            for i in range(index, len(nums)):
                subset.append(nums[i])
                answer.append(subset.copy())
                backtrack(i+1, subset)
                subset.pop()
        backtrack(0, [])
        return answer
                
                
        