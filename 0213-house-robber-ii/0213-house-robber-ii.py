class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        dp1 = nums[:len(nums)-1]
        dp1[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            dp1[i] = max(dp1[i-1],dp1[i-2]+nums[i])
        
        
        dp2 = nums[1:len(nums)]
        print(dp2)
        dp2[1] = max(nums[1],nums[2])
        for i in range(2,len(nums)-1):
            dp2[i] = max(dp2[i-1],dp2[i-2]+nums[i+1])
        return max(dp1[-1],dp2[-1])
        