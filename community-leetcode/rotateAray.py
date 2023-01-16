class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)

        if l == k: return
        
        k = k % l
        
        j = l - 1
        for i in range(l//2):
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        
        j = k - 1
        for i in range(k//2):
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1

        
        j = l - 1
        for i in range(k, k + (l - k)//2):
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
