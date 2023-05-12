class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*len(quiet)
        answer = [i for i in range(len(quiet))]
        
        for start, end in richer:
            graph[start].append(end)
           
            indegree[end] += 1
        
        queue = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            parent = queue.popleft()
            for child in graph[parent]:
                indegree[child] -= 1
                
                if quiet[parent] <= quiet[child]:
                    answer[child] = answer[parent]
                    quiet[child] = quiet[parent]
                
                
                if indegree[child] == 0:
                    queue.append(child)
        
        return answer
            