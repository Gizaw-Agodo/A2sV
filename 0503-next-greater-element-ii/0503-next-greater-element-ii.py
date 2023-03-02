class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        nums = nums*2
        next_greater = [-1]*len(nums)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                next_greater[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        return next_greater[:len(nums)//2]
                