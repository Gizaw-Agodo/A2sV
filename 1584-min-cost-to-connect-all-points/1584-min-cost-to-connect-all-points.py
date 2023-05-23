class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
      
        parent = list(range(len(points)))
        size = [1 for _ in range(len(points))]
       
        def find(x):
            if x != parent[x]:
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
            
        heap = []
        for i in range(len(points)):
            x,y = points[i]
            for j in range(i + 1, len(points)):
                    u,v = points[j]
                    distance = abs(u-x) + abs(v-y)
                    heappush(heap,[distance, i,j])
            
        totalDistance = 0
        index = len(heap)
        
        while index > 0:
            d, point1, point2 = heappop(heap)
            
            parent1 = find(point1)
            parent2 = find(point2)
            
            if parent1 != parent2:
                totalDistance += d
                union(point1, point2)
                
            index -= 1
                
        return totalDistance      
