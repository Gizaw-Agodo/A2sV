class Solution(object):
    def minimumBuckets(self, street):
        """
        :type street: str
        :rtype: int
        """
        n = len(street)
        status = [0]*n
        
        for i in range(n) :
            if street[i]=="H":
                if i>0 and status[i-1] ==1 :
                    continue
                elif i+1  < n  and street[i+1] == ".":
                    status[i+1] =1 
                elif i> 0 and  street[i-1] ==".":
                    status[i-1] = 1
                else:
                    return -1
        return status.count(1)
                    
