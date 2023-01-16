class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i =0
        j=len(nums)-2
        while i<=j:
            if nums[j]==0:
                nums.append(nums.pop(j))
                j-=1
            if nums[i]==0:
                nums.append(nums.pop(i))
                j-=1
            if nums[j]!=0 and nums[i]!=0:
                i+=1
                j-=1
            
