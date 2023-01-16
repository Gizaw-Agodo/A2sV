class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dq=deque([(nums[0],0)])
        for i in range(1,len(nums)):
            score=dq[0][0]+nums[i]
            while dq and dq[-1][0]<score: dq.pop()
            dq.append((score,i))
            if dq[0][1]==i-k: dq.popleft()
        return dq[-1][0]
