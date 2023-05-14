class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for a,b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        queue = deque([])
        for  items in indegree.items():
            if items[1] == 1:
                queue.append([items[0], 'inf'])
                break
        
        order = []
        while queue:
            child, parent = queue.popleft()
            order.append(child)
            for neibhour in graph[child]:
                if neibhour != parent:
                    indegree[neibhour] -= 1
                    if indegree[neibhour] <= 1:
                        queue.append([neibhour, child])
                        
        return order
            
            
        
        
        
        