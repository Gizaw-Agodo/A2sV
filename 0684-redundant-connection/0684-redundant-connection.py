class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(len(edges) + 1))
        size = [1]*(n + 1)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            xroot = find(x)
            yroot = find(y)
            
            if xroot == yroot:
                return True
            else:
                if size[xroot] >= size[yroot]:
                    parent[yroot] = xroot
                    size[xroot] += size[yroot]
                else:
                    parent[xroot] = yroot
                    size[yroot] += size[xroot]
            return False
        
        for start, end in edges:
            if union(start, end):
                return [start, end]