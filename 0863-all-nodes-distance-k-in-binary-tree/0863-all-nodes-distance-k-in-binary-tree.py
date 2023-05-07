# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
       
        graph = defaultdict(list)
        stack = deque([root])
        visited = set([root.val])
        
        current = root
        while stack :
            
            node = stack.popleft()
            if node.left and node.left.val not in visited:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                stack.append(node.left)
                
            if node.right and node.right.val not in visited:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                stack.append(node.right)
        
        stack = deque([[target.val, 0]])
        visited = set([target.val])
        
        answer = []
        def bfs (graph, k):
            
            while stack:
                
                node, d = stack.popleft()
                if d == k :
                    answer.append(node)
                    
                for child in graph[node]:
                    if child not in visited : 
                        visited.add(child)
                        stack.append([child, d + 1])
                       
        bfs(graph, k)
        return answer
            
            
                
                
    
        