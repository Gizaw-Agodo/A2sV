class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1 for i in range(n)]
 
        temp = 1
        for i in range(n):
            result[i] = temp
            temp *= nums[i]

        temp = 1

        for i in range(n - 1, -1, -1):
            result[i] *= temp
            temp *= nums[i]

    
        return result
