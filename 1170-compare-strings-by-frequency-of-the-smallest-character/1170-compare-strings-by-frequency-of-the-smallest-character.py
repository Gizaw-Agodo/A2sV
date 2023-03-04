class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def findFrequency(word):
            count = Counter(word)
            minChar = min(count.keys())
            return count[minChar]
        
        def findCount(query, words):
            left = 0
            right = len(wordsFrequency)-1
            while left <= right:
                mid = left + (right - left)//2
                if words[mid] > query:
                    right = mid - 1
                elif words[mid] <= query:
                    left = mid + 1
            return len(words)-right-1
        
        
        wordsFrequency = []
        queryFrequency = []
        for word in words : 
            curr_frequency = findFrequency(word)
            wordsFrequency.append(curr_frequency)
        for query in queries :
            curr_frequency = findFrequency(query)
            queryFrequency.append(curr_frequency)
      
        answer = []
        wordsFrequency.sort()
        print(queryFrequency)
        for count in queryFrequency:
            curr_count = findCount(count, wordsFrequency)
            answer.append(curr_count)
        return answer
            
       
            

        
        