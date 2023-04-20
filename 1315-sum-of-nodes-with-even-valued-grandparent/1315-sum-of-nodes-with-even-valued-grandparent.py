# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        total = 0
        def dfs(node,curr_count):
            nonlocal total
            if not node:
                return [curr_count , 0]
            if curr_count == 2:
                return [curr_count, node.val] 
            
            lcount, lvalue  = dfs(node.left, curr_count + 1)
            if lcount == 2:
                total += lvalue
            rcount, rvalue  = dfs(node.right, curr_count + 1)
            if rcount == 2:
                total += rvalue
            
            return [curr_count,node.val]
        
        def tree(node):
            if not node :
                return 
            if node.val % 2 == 0:
                dfs(node,0)
                
            tree(node.left)
            tree(node.right)
            
        tree(root)
        return total
            
            