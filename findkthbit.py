class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        current='0'
        now='0'
        oppo='1'
        while n-1>0:
            current=now+'1'+oppo
            oppo=now+'0'+oppo
            now=current
            n-=1
        #print(current)
        return current[k-1]
