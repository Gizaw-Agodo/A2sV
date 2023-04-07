class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = defaultdict(list)
        for start, dest in edges:
            dic[start].append(dest)
            dic[dest].append(start)
        
        def dfs(graph, visited,node):
            if node == destination:
                return True
            visited.add(node)
            for neibhor in graph[node]:
                if neibhor not in visited:
                    found = dfs(graph,visited,neibhor)
                    if found:
                        return True
            return False
        return dfs(dic,set(),source)
        