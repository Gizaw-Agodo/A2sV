class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        count = 0
        cursum = 0
        for n in nums :
            cursum +=n
            if cursum == k :
                count +=1
            if cursum-k in dic :
                count += dic[cursum-k]
            if cursum in dic :
                dic[cursum] +=1
            else:
                dic[cursum] = 1
        return count
                
