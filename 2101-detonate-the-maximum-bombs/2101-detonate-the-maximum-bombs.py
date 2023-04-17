class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        adj_list = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                x1, y1, r1 = bombs[i]
                x2 ,y2 ,r2 = bombs[j]
                if  sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2) <= r1 and i != j:
                    adj_list[i].append(j)
                    
                    
        def dfs(root):
            visited.add(root)
            curr_max = 1
            for child in adj_list[root]:
                if child not in visited:
                    curr_max +=  dfs(child)  
            return curr_max
        
        maximum  = 1
        for key in adj_list.copy():
            visited = set()
            if key not in visited:
                maximum = max(maximum,dfs(key))    
        return maximum
                    
        