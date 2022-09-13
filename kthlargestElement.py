class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        k_thmax = 0
        for i in range(k):
            k_thmax = heapq.heappop(heap)
        return -(k_thmax)
