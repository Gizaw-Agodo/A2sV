class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        parent = list(range(n))
        size = [1]*n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            xroot = find(x)
            yroot = find(y)
            
            if size[xroot] >= size[yroot]:
                parent[yroot] = xroot
                size[xroot] += size[yroot]
            else:
                parent[xroot] = yroot
                size[yroot] += size[xroot]
        
        for start, end in edges:
            union(start, end)
                
        return find(source) == find(destination)