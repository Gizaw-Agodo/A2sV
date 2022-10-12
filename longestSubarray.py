class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = 0
        deleted = 0
        slow,fast = 0,0
        while fast < n :
            if nums[fast] == 0 :
                if deleted == 0 :
                    deleted +=1
                else:
                    maximum = max(maximum,fast-slow-1)
                    if nums[slow] == 0 :
                        deleted -=1
                    slow +=1
                    fast -=1
            fast +=1
        if deleted == 1:
            maximum = max(maximum,fast-slow-1)

            
        if deleted == 0 :
            return n-1
        else:
            return maximum
