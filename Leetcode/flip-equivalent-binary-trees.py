# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root1, root2):
            if root1 is None and root2 is None:
                return True
            
            if root1 is None or root2 is None:
                return False

            if root1.val != root2.val:
                return False
            
            case1 = dfs(root1.left, root2.left)
            case2 = dfs(root1.right, root2.right)
            case3 = dfs(root1.left, root2.right)
            case4 = dfs(root1.right, root2.left)

            return (case1 and case2) or (case3 and case4)
        
        return dfs(root1, root2)

  
