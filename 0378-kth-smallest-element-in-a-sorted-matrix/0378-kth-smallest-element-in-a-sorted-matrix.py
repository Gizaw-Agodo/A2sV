class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heappush(heap, matrix[i][j])
        
        for i in range(k-1):
            heappop(heap)
        return heap[0]