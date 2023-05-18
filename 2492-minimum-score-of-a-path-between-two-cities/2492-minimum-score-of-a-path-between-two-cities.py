class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = list(range(n + 1))
        size = [1]*(n + 1)
        minDistance = [float('inf') for i in range(n + 1)]
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            xroot = find(x)
            yroot = find(y)
            childMin = min(minDistance[x],minDistance[y])
            rootMin = min(minDistance[xroot],minDistance[yroot])
            
            if size[xroot] >= size[yroot]:
                
                parent[yroot] = xroot
                minDistance[xroot] = min(childMin,rootMin)
                size[xroot] += size[yroot]
            else:
                parent[xroot] = yroot
                minDistance[yroot] = min(childMin,rootMin)
                size[yroot] += size[xroot]
                
        for start, end ,weight in roads:
            minDistance[start] = min(weight,minDistance[start])
            minDistance[end] = min(weight,minDistance[end])
            union(start, end)
        
        return minDistance[find(1)]