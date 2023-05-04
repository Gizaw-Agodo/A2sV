class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heappush(heap, -1*stones[i])
        
        while len(heap) >= 2:
            y = heappop(heap)
            x = heappop(heap)
            if abs(x) < abs(y):
                heappush(heap, -1 * (abs(y) - abs(x)))
        
        return abs(heap[-1]) if len(heap) > 0 else 0
            