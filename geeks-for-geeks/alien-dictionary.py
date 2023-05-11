#User function Template for python3
from collections import defaultdict
from collections import deque

class Solution:
    def findOrder(self,alien_dict, N, K):
        
    
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for i in range(k):
            indegree[chr(97 + i)] = 0
        
        for i in range (N-1):
            word1 = alien_dict[i]
            word2 = alien_dict[i + 1]
            
            p1 = p2 = 0
            while p1 < len(word1) and p2 < len(word2):
                if word1[p1] == word2[p2]:
                    p1 += 1
                    p2 += 1
                    continue
                else:
                    graph[word1[p1]].append(word2[p2])
                    indegree[word2[p2]] += 1
                    break
        
        queue = deque([])

        for key in indegree :
            if indegree[key] == 0:
                queue.append(key)
        
        order = []
       
        while queue:
            value = queue.popleft()
            order.append(value)
            for child in graph[value]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    
        return order   
