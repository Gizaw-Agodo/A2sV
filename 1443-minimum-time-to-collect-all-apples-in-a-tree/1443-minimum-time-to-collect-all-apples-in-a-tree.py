class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        
        for i, j in edges:
            tree[i].append(j)
            tree[j].append(i)
        
        def dfs(node, parent):
            
            total = 0
            
            for child in tree[node]:
                if child == parent:
                    continue
               
                total += dfs(child, node)
            
            if node != 0 and (total > 0 or hasApple[node]):
                total += 2
                
            return total
                    
               
        return dfs(0, 0)
                