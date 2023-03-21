class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def backtrack(index, comb):
            if len(comb) >= 2:
                answer.append(comb.copy())
                
            for i in range(index, len(nums)):
                if len(comb) == 0 or comb[-1] <= nums[i]:
                    comb.append(nums[i])
                    backtrack(i + 1, comb)
                    comb.pop()
                    
        backtrack(0, [])
        output = Counter([tuple(i) for i in answer])
        return [list(key) for key in output]
       
