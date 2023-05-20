class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        size =  {}
        parent = {}
        
        for x,y in stones:
            x, y = f'x{x}',f'y{y}'
            size[x], size[y] = 1, 1
            parent[x], parent[y] = x, y
            
        
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
       
        for x, y in stones:
            union(f'x{x}', f'y{y}')
        
        unremoved = sum(parent[element] == element for element in parent)
        return len(stones) - unremoved

            
            
                
        
            
                
            
        
        