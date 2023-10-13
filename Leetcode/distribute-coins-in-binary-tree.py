# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
       
        moves = 0
        def dfs(node):
            nonlocal moves
            if node is None:
                return 0
            
            currVal = node.val - 1
            leftVal = dfs(node.left)
            rightVal = dfs(node.right)

            currVal += leftVal + rightVal 
            moves += abs(currVal)
            return currVal
            
        dfs(root)
        return moves
