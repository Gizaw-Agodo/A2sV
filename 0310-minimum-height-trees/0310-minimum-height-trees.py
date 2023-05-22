class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        queue  = deque([])
        indegree = [0]*n
        answer = []
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            indegree[start] += 1
            indegree[end] += 1
            
        
        for i in range(len(indegree)):
            if indegree[i] == 1:
                queue.append(i)
     
        while queue:
            
            length = len(queue)
            answer = []
            for i in range(length):
                node = queue.popleft()
                answer.append(node)
                
                for child in graph[node]:
                    indegree[child] -= 1
                    if indegree[child] == 1:
                        queue.append(child)
       
        if n == 1 :
            answer.append(0)
            return answer
                    
        return answer
                        
                
            