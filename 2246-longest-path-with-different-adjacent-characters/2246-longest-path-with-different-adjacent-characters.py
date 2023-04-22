class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        adge_list = defaultdict(list)
        for i in range(len(parent)):
            adge_list[parent[i]].append(i)
        
        longest_path = 0
        
        def dfs(parent):
            nonlocal longest_path
            
            first_max = 0
            second_max = 0
            
            for child in adge_list[parent]:
                
                pathlen = dfs(child)
                if s[child] != s[parent]:
                    if pathlen > first_max:
                        second_max = first_max
                        first_max = pathlen
                    else:
                        second_max = max(second_max, pathlen)
                        
            pathsum = first_max + second_max
            longest_path = max(longest_path, pathsum)
            
            return first_max + 1
       
        dfs(0)
        return longest_path + 1
        