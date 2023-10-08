# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        answer = []
        def dfs(node, path, curr_sum):
            
            path.append(node.val)

            if node.left == None and node.right == None:
                if curr_sum + node.val == targetSum:
                    answer.append(path[:])
                    
            
            if node.left:
                dfs(node.left, path, curr_sum + node.val)
            
            if node.right:
                dfs(node.right, path, curr_sum + node.val)
            
            path.pop()

        if root == None:
            return []  
        
        dfs(root, [], 0)
        return answer
            

        
