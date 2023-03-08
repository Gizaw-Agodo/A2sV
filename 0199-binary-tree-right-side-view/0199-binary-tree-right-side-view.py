# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # print(root.val,root.right.val,root.left)
        answer = defaultdict(int)
        def findLevel(root, level):
            if root == None:
                return 
            answer[level] = root.val
            findLevel(root.left, level + 1)
            findLevel(root.right, level + 1)
        
        findLevel(root,0)
        return answer.values()
      