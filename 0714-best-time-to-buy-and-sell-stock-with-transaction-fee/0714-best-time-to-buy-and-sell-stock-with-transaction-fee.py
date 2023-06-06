class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell = [0]*len(prices)
        buy = [0]*len(prices)
        sell[0],buy[0] = 0,-prices[0]
        
        if len(prices) <= 1:
            return 0
        
        for i in range(1, len(prices)):
            buy[i] = max(buy[i-1],sell[i-1] - prices[i])
            sell[i] = max(sell[i-1],buy[i-1] + prices[i] - fee) 
        return sell[-1]