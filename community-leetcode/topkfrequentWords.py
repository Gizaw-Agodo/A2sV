class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dic = defaultdict(int)
        for word in words :
            dic[word]+=1
            
        heap = []
        for word,count in dic.items():
            heapq.heappush(heap,(-count,word))
        
        res = []
        while len(res) < k:
            count,word = heapq.heappop(heap)
            res.append(word)
        return res
