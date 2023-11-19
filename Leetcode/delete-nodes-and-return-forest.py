# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        answer = []

        def dfs (root):

            if root is None:
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if root.val in to_delete:
                if root.left == None and root.right == None:
                    return None
                
                if root.left : 
                    answer.append(root.left)
                if root.right:
                    answer.append(root.right)
                return None
                
            return root
        
        updated_root = dfs(root)
        if updated_root:
            answer.append(updated_root)
        return answer
                

