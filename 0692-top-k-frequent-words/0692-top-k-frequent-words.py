class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
       
        for key, count in counter.items():
            heappush(heap, [-1 *count, key])
       
        answer = []
        for i in range(k):
            count, key = heappop(heap)
            answer.append(key)
            
        return answer