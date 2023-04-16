class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(set)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i == j and i not in graph:
                    graph[i] = set()
                    
                if i != j and isConnected[i][j]:
                    graph[i].add(j)            
                    
        visited = set() 
        def dfs(node):
            visited.add(node)
            for neibhour in graph[node]:
                if neibhour not in visited:
                    dfs(neibhour)
                 
        count = 0
        for node in graph:
            if node not in visited:
                dfs(node)
                count += 1
                
        return count
       
            
        
        
        
        