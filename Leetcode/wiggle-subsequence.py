class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        wiggle = [(0,0)]*len(nums)
        wiggle[0] = (1,1)

        for i in range(1,len(nums)):
            up, down = wiggle[i-1]
            currUp = up
            currDown = down
            if nums[i] < nums[i-1]:
                currUp = down + 1
            if nums[i] > nums[i-1]:
                currDown = up + 1
            wiggle[i] = (currUp, currDown)
        return max(wiggle[-1][0],wiggle[-1][1])
            

        