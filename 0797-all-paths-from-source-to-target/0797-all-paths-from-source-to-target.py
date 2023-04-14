class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(list)
        for i in range(len(graph)):
            adj_list[i] = graph[i]
          
        paths = []
    
        def dfs(node,temp_path):
            
            temp_path.append(node)
            if node == len(graph)-1:
                paths.append(temp_path.copy())
                
            for child in adj_list[node]:
                dfs(child,temp_path)
                temp_path.pop()
                
            
        dfs(0,[])
        return paths
        
        