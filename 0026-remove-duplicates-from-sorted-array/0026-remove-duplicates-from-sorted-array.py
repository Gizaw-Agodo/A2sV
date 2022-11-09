class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow,fast = 1,1
        temp = nums[0]
        while fast < len(nums):
            if temp != nums[fast]:
                nums[slow] = nums[fast]
                temp = nums[fast]
                slow +=1
            fast +=1
        return slow