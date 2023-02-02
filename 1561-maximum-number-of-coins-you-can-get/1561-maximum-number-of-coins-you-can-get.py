class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        maximum = 0
        i = len(piles)-2
        while  i >= len(piles)//3 :
            maximum += piles[i]
            i-=2
        return maximum