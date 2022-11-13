class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        answer = []
        dic = defaultdict(int)
        for i in range(len(items1)):
            dic [items1[i][0]] += items1[i][1]
            
        for i in range(len(items2)):
            dic [items2[i][0]] += items2[i][1]
        print(dic)
        for i in dic:
            answer.append([i,dic[i]])
        answer.sort()
        return answer