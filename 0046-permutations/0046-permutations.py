class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def backtrack(k, combination):
            if k == 0:
                answer.append(combination.copy())
            
            for i in range(len(nums)):
                if nums[i] in combination:
                    continue 
                combination.append(nums[i])
                backtrack(k-1, combination)
                combination.pop()
            
        backtrack(len(nums), [])
        return answer