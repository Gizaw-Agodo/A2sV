class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        n = len(security)
        after = [0]*n
        before = [0]*n
      
        
        for i in range(n-2,-1,-1):
            if security[i]<= security[i+1]:
                after[i] = 1+after[i+1] 
        
        for i in range (1,n):
            if security[i-1] >= security[i]:
                before[i] = 1+before[i-1]
        res  = []
      
        for k in range(n):
            if before[k] >= time and after[k]>=time:
                res.append(k)
        return res
                
