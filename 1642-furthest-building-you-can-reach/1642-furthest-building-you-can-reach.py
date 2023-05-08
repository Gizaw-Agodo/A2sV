class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff <=0 :
                continue
            heapq.heappush(heap,-diff)
            bricks -= diff
            print(diff,bricks)
            if bricks < 0 and ladders == 0:
                return i
            if bricks < 0:
                ladders -= 1
                bricks -= heapq.heappop(heap)
        return n-1