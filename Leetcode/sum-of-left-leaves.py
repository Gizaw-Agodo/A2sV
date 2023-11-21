# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root, dir):
            if root == None:
                return 0
            if root.left == None and root.right == None and dir == "L":
                return root.val

            curr_sum = 0
            curr_sum += dfs(root.left, "L")
            curr_sum += dfs(root.right, "R")

            return curr_sum

        return dfs(root, None)
        