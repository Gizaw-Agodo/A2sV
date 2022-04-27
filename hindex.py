class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)

        citations.sort()

        for i, citation in enumerate(citations):
            if citation >= n - i:
                return n - i

        return 0
        
