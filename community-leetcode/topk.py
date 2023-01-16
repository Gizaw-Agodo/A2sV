class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}
       
        for element in nums :
            if element in frequency:
                frequency[element] +=1
            else:
                frequency [element] = 1
        return sorted(frequency,key = frequency.get ,reverse = True) [:k]
