class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        maximum = 0
        max_start = len(piles)//3 
        i = len(piles)-2
        while  i >= max_start:
            maximum += piles[i]
            i-=2
        return maximum