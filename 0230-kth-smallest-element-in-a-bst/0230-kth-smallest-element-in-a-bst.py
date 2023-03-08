# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    minimum = float("inf")
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def traverse(node, k):
            if not node or len(values) >= k:
                return

            traverse(node.left, k)
            values.append(node.val)
            traverse(node.right, k)

        traverse(root, k)
        return values[k - 1]
      
            
            