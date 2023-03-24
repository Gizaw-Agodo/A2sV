class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != -1:
                if nums[i] == nums[nums[i]-1]:
                    nums[i] = -1
                else:
                    nums[nums[i]-1], nums[i] = nums[i],nums[nums[i]-1]
        for i in range(len(nums)):
            if nums[i] == -1:
                ans.append(i+1)
        return ans