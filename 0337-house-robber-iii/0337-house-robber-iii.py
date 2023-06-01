# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dfs(node):
            if node == None :
                return 0
        
            
            if_robed = node.val
            if node.left :
                if_robed  += dfs(node.left.right) + dfs(node.left.left)
            if node.right:
                if_robed += dfs(node.right.left) + dfs(node.right.right)
            
            if_not_robed = 0
            if_not_robed += dfs(node.left) + dfs(node.right)
            
            maximum = max(if_robed,if_not_robed)
            
            return maximum
            
        return dfs(root)
            
                