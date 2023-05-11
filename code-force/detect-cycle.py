from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		color = [0]*len(adj)
		
		for i in range(len(adj)):
		    if color[i] != 0:
		        continue
		    if not self.dfs(adj, color, i,float('inf')):
		        return True
		        
		return False
	
	def dfs(self, adj, color, node, parent):
	    
	    if color[node] == 1:
	        return False
	    
	    color[node] = 1
	    for child in adj[node]:
	        if color[child] == 2 or child == parent:
	            continue
	        if not self.dfs(adj, color, child, node):
	            return False
	    color[node] = 2
