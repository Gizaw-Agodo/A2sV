class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = list(range(n + 1))
        size = [1]*(n + 1)
        minDistance = [float('inf') for i in range(n + 1)]
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y,weight):
            xroot = find(x)
            yroot = find(y)
            rootMin = min(minDistance[xroot],minDistance[yroot])
            
            if size[xroot] >= size[yroot]:
                
                parent[yroot] = xroot
                minDistance[xroot] = min(weight,rootMin)
                size[xroot] += size[yroot]
            else:
                parent[xroot] = yroot
                minDistance[yroot] = min(weight,rootMin)
                size[yroot] += size[xroot]
                
        for start, end ,weight in roads:
            union(start, end,weight)
        
        return minDistance[find(1)]