class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        answer = -1
        visited = [False]*len(edges)
        
        def dfs(node, distance, visited):
            nonlocal answer
            
            visited[node]  = True
            
            child = edges[node]
            
            if visited[child] == False and child != -1:
                distance[child] = distance[node] + 1
                return dfs(child, distance, visited)
            
            elif child != -1 and child in distance:
                diff = distance[node] - distance[child] + 1
                answer = max(answer, diff ) 
        
        
        for i in range(len(edges)):
            
            if visited[i] == False:
                dfs(i, {i:1}, visited)
     
        return answer
            