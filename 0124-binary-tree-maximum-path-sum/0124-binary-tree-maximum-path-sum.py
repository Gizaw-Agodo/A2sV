# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathSum = float('-inf')
        
        def dfs(node):
            nonlocal maxPathSum
            
            if not node:
                return 0
            
            lsum = max(dfs(node.left),0)
            rsum = max(dfs(node.right),0)
            
            maxPathSum = max(maxPathSum, node.val + lsum + rsum)
            
            return node.val + max(lsum, rsum)
    
        dfs(root)
        
        return maxPathSum