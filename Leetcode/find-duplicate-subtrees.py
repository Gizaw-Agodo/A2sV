# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        nodes = defaultdict(int)
        answer = set()
        
        def dfs (root):
        
            if root is None:
                return "#"

            tree =  str(root.val) 
            tree += "," + dfs(root.left)
            tree += "," + dfs(root.right)
            
            nodes[tree] += 1

            if nodes[tree] == 2:
                answer.add(root)
           
            return tree
        dfs(root)
 
        return list(answer)
                 
        
