class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        order = []
       
        while queue:
            value = queue.popleft()
            order.append(value)
            for child in graph[value]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    
        return len(order) == numCourses
            
            