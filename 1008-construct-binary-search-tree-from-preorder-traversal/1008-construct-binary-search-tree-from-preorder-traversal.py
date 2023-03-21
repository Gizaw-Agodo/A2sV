# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
    
        root = TreeNode(float('inf'))
        stack = [root]
        
        for value in preorder:
            node = TreeNode(value)
            if stack and stack[-1].val > value:
                stack[-1].left = node
            else:        
                while len(stack) > 1 and stack[-2].val < node.val:
                    stack.pop()
                stack[-1].right = node
                stack.pop()
            stack.append(node)
        return root.left
            
