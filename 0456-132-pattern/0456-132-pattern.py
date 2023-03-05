class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        num3 = float("-inf")
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < num3:
                return True
            while stack and nums[i] > stack[-1] : 
                num3 = stack.pop()
            stack.append(nums[i])
        return False
                
       