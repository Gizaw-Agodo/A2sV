# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkValid(root, minn, maxx):
            if root == None:
                return True
            if root.val <= minn:
                return False
            if root.val >= maxx:
                return False
            left = checkValid(root.left, minn, root.val)
            right = checkValid(root.right, root.val, maxx)
            
            return left and right
        
        return checkValid(root,float("-inf"),float("inf"))

          
        