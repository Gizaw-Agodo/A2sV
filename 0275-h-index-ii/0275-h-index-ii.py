class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start = 0
        end = len(citations)-1
        while start <= end:
            mid = start + (end-start)//2
            if citations[mid] >= len(citations) - mid:
                end = mid - 1
            elif citations[mid] < len(citations) - mid:
                start = mid + 1
                
        return len(citations) - start
                