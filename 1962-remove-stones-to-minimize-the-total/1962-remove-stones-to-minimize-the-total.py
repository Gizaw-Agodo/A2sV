class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for elem in piles:
            heapq.heappush(heap,-elem)
        for i in range(k):
            largest = -heapq.heappop(heap)
            removed = floor((largest/2))
            heapq.heappush(heap,-1*(largest-removed))
        
        return -sum(list(heap))