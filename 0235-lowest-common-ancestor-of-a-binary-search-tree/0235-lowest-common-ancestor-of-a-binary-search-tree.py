# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    lowCommon = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        lowest_ancesstor = defaultdict(int)
        
        def searchNode(root, val):
            if root == None:
                return None
            lowest_ancesstor[root] += 1
            if lowest_ancesstor[root] == 2 :
                self.lowCommon = root
            if root.val < val:
                return searchNode(root.right,val)
            if root.val > val:
                return searchNode(root.left,val)
        
        searchNode(root,p.val)
        searchNode(root,q.val)
        
        return self.lowCommon

        
       

