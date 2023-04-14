# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        strings = []
        def dfs(root):
            if root == None:
                return 
            
            strings.append(str(root.val))
            if root.left or root.right:
                strings.append("(")
                dfs(root.left)
                strings.append(')')
            
            if root.right:
                strings.append('(')
                dfs(root.right)
                strings.append(')')
        dfs(root)
        return "".join(strings)
            
        