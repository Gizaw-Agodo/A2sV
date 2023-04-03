class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def xOr(arr):
            ans = 0
            for i in range(len(arr)):
                ans |= arr[i]
            return ans 
        
        subsets = []
        def backtrack(subset, index):
            if len(subset) == len(nums):
                subsets.append(subset.copy())
                return 
            subsets.append(subset.copy())
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()
        backtrack([], 0)
        
        maxXor = xOr(nums)
        count = 0
        for item in subsets:
            xor = xOr(item)
            if xor == maxXor:
                count += 1
        return count
    
            