class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0]*n
        
        for i,j in edges:
            indegree[j] += 1
            graph[i].append(j)
        
        answer = [set() for _ in range (n)]
        
        queue = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            value = queue.popleft()
            for child in graph[value]:
                newset = answer[child].union(answer[value])
                newset.add(value)
                answer[child] = newset
                
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
         
        for i in range(len(answer)):
            answer[i] = list(answer[i])
            answer[i].sort()
        return answer