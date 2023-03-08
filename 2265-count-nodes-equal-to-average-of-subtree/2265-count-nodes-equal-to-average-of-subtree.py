# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    node_count = 0
    average_count = 0
    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def findSum(node):
            if node == None:
                return 0
            self.node_count += 1
            leftsum  = node.val +  findSum(node.left)
            rightsum = findSum(node.right)
            return leftsum + rightsum
        
        def findNodes(node):
            if node == None:
                return 
            node_sum = findSum(node)
            if floor(node_sum/self.node_count) == node.val:
                self.average_count += 1
            self.node_count = 0 
            findNodes(node.left)
            findNodes(node.right)
            
        findNodes(root)
        return self.average_count
        