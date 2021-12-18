class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        for _ in range(len(nums)):
            if nums[curr] == 0:
                nums.pop(curr)
                nums.insert(0, 0)
                curr += 1
            elif nums[curr] == 2:
                nums.pop(curr)
                nums.append(2)
            else:
                curr += 1
        return
