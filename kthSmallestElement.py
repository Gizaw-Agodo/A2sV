class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix[0])
        count = 0
        heap = []
        for i in range(n):
            for j in range(n):
                if count <k:
                    heapq.heappush(heap,-matrix[i][j])
                    count +=1
                elif -heap[0] > matrix[i][j]:
                    heapq.heappop(heap)
                    heapq.heappush(heap , -matrix[i][j])
                   
        return -heap[0]
        
