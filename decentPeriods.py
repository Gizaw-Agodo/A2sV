class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        smoothes = {}
        smoothes[n-1] = 1
        for i in range(n-2,-1,-1):
            if prices[i+1]==prices[i]-1:
                smoothes[i] = 1 +smoothes[i+1]
            else:
                smoothes[i] = 1
        returned = 0
        for i in range(len(smoothes)):
            returned += smoothes[i]
        return returned
