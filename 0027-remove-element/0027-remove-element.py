class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow,fast = 0,0
        while fast < len(nums):
            if nums[fast] == val:
                fast +=1
                continue
            nums[slow] = nums[fast]
            slow+=1
            fast +=1
        return slow