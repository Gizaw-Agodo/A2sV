class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        parent = list(range(len(source) + 1))
        size = [1 for _ in range(len(source) + 1)]
       
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
        
        for a,b in allowedSwaps:
            union(a + 1,b + 1)
            
        tree = defaultdict(set)
      
        for i in range(1,len(parent)):
            tree[find(i)].add(i)
       
    
        answer = 0
        for indices in tree.values():
            
            A = [source[i-1] for i in indices]
            B = [target[i-1] for i in indices]
      
            answer += sum((Counter(A) - Counter(B)).values())
        
        return answer  
            
 