class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i]%2
        
        dic = {}
        presum = 0
        count = 0
        for num in nums :
            presum += num
            if presum == k :
                count +=1
            if presum - k in dic :
                count += dic[presum-k]
            if presum in dic :
                dic[presum] +=1
            else:
                dic[presum] = 1
        return count
                
