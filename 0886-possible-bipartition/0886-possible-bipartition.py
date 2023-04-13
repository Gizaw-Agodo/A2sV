class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # generate adjecency_list graphh 
        adj_list = defaultdict(list)
        for a, b in dislikes:
            adj_list[a - 1].append(b - 1)
            adj_list[b - 1].append(a - 1)
        
        #define array to hold the color of each element of graph
        color = [-1]*n
    
        def dfs(node , cur_color):
            color[node] = cur_color
            for neibhour in adj_list[node]:
                if color[neibhour] == cur_color:
                    return False
                elif color[neibhour] == -1:
                    if not dfs(neibhour, 1 - cur_color):
                        return False
            return True
        
        for node in adj_list:
            if color[node] == -1:
                if not dfs(node, 0):
                    return False   
        return True
                
                
        
        
        
        
        
            
        
        