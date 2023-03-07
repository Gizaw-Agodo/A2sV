# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkSymmetric(left, right):
            if left == None and right == None:
                return True
            if (left == None and right) or (right == None and left):
                return False
            if  left.val != right.val: 
                return False 
        
            check_left = checkSymmetric(left.right,right.left)
            check_right = checkSymmetric(left.left,right.right)
        
            if  check_left and check_right:
                return True
            else:
                return False
            
        return (checkSymmetric(root.left, root.right))
    
        