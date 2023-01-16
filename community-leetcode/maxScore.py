class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        total = sum(cardPoints)
        
        remaining_length = n - k
        subarray_sum = sum(cardPoints[:remaining_length])
        
        min_sum = subarray_sum
        for i in range(remaining_length, n):
            subarray_sum += cardPoints[i]
            subarray_sum -= cardPoints[i - remaining_length]
            min_sum = min(min_sum, subarray_sum)
        return total - min_sum
