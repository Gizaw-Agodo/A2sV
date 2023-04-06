class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic = defaultdict(int)
        for source, end in edges:
            dic[source] += 1
            dic[end] += 1
        maximum = float("-inf")
        answer = -1
        for key in dic :
            if dic[key] > maximum:
                maximum = dic[key]
                answer = key
        return answer
            
           