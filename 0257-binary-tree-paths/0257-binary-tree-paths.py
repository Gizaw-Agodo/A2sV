# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        def backtrack(path, root):
            if root == None:
                return 
            
            if not root.left and not root.right:
                path.append(root.val)
                answer.append("->".join(map(str,path.copy())))
                path.pop()
                return
                
            if root.left :
                path.append(root.val)
                backtrack(path, root.left)
                path.pop()
                    
            if root.right :
                
                path.append(root.val)
                backtrack(path, root.right)
                path.pop()
            
        backtrack([], root)
        return answer