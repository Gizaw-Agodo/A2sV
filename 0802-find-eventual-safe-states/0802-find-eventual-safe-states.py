class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = [0]*len(graph)
        
        def dfs(graph, node, colors):
            
            if colors[node] == 1:
                return False
            
            colors[node] = 1
            for child in graph[node]:
                if colors[child] == 2:
                    continue
                if not dfs(graph, child, colors):
                    return False
            
            colors[node] = 2
            return True
        
        for i in range(len(graph)):
            
            if colors[i]!=0:
                continue
            dfs(graph, i, colors)
            
        answer  = []
        for i in range(len(colors)):
            if colors[i] == 2:
                answer.append(i)
        return answer
            
            