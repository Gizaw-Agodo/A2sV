  def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        len1 = firstLen+secondLen
        sumfirst = 0
        sumsecond = 0 
        for i in range(len1):
            if i < firstLen:
                sumfirst+=nums[i]
            else:
                sumsecond+=nums[i]
        ans = sumfirst+sumsecond
        maximum = sumfirst
        
        for i in range(len1 ,len(nums)):
           
            sumsecond += nums[i]- nums[i-secondLen]
            sumfirst += nums[i-secondLen]-nums[i-(len1)]
            maximum = max(maximum,sumfirst)
            ans =max(ans,maximum+sumsecond)
            
        return ans
