class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        minh, maxh = [], []
        l, r  = 0, 0
        ret = 0
        
        while r < len(nums):
            heapq.heappush(minh, (nums[r],r))
            heapq.heappush(maxh, (-nums[r],r))
            
            while -maxh[0][0] - minh[0][0] > limit:
                l = min(maxh[0][1], minh[0][1]) + 1
                while maxh[0][1] < l:
                    heapq.heappop(maxh)
                while minh[0][1] < l:
                    heapq.heappop(minh)
            
            ret = max(ret, r - l + 1)
            r += 1
        return ret
