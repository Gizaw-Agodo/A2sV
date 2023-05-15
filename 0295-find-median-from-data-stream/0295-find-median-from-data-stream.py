class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        
    def addNum(self, num: int) -> None:
        
        heappush(self.maxHeap, -1*num) 
        value = heappop(self.maxHeap)
        heappush(self.minHeap, -1*value)
        
        if len(self.minHeap) > len(self.maxHeap):
            value = heappop(self.minHeap)
            heappush(self.maxHeap, -1*value)
       
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-1*self.maxHeap[0] + self.minHeap[0])/2
        
        return -1*self.maxHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()