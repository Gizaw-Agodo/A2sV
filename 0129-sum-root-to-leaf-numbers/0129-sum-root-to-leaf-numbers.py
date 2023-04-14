# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:     
        total = 0    
        def dfs(node, path_sum):
            nonlocal total 
            if not node:
                return 
            path_sum.append(str(node.val))
            if not node.left and not node.right:
                total += int("".join(path_sum))
                path_sum.pop()
                return
            dfs(node.left, path_sum)
            dfs(node.right, path_sum)
            path_sum.pop()
                
        dfs(root, [])
        return total
            