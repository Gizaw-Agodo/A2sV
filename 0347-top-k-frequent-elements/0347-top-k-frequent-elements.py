class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
       
        for element in nums :
            if element in frequency:
                frequency[element] +=1
            else:
                frequency [element] = 1
        return sorted(frequency,key = frequency.get ,reverse = True) [:k]