class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        
        while len(heap) >1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x != y :
                heapq.heappush(heap,y-x)

        if len(heap) == 0:
            return 0
        return -(heapq.heappop(heap))
