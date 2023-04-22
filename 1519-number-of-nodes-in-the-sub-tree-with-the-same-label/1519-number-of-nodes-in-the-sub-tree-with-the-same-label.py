class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
       
        # defining edge list of the graph
        edge_list = defaultdict(list)
        for node1, node2 in edges:
            edge_list[node1].append(node2)
            edge_list[node2].append(node1)
        
        # array to hold the labels count
        answer = [0]*n
        
        def dfs(prev, curr):
            
            # array to store the count of each label in sub tree
            ans = [0]*26
          
            ans[ord(labels[curr]) - ord('a')] += 1
            
            for child in edge_list[curr]:
                if child != prev:
                    result = dfs(curr, child)
                    for i in range(26):
                        ans[i] += result[i]
                        
            answer[curr] += ans[ord(labels[curr]) - ord('a')]
            return ans
               
        dfs(-1, 0)
        return answer