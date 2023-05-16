class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        preRequesit  = defaultdict(set)
        indegrees = [0]*numCourses
        queue = deque([])
        
        for a, b in prerequisites:
            graph[a].append(b)
            indegrees[b] += 1
      
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
                preRequesit[i] = set()
                
        while queue:
            current = queue.popleft()
            
            for child in graph[current]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)
                preRequesit[child].add(current)
                temp = preRequesit[child].union(preRequesit[current])
                preRequesit[child] = temp
             
      
        answer = [False]*len(queries)
        for i in range(len(queries)):
            a,b = queries[i]
            if a in preRequesit[b]:
                answer[i] = True
        print(preRequesit)      
        return answer
                
                
                