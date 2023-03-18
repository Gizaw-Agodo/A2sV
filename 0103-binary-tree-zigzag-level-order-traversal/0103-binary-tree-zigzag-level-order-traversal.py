# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = defaultdict(list)
        def findLevel(root, level):
            if root == None:
                return 
            answer[level].append(root.val)
            findLevel(root.left, level + 1)
            findLevel(root.right, level + 1)
        
        findLevel(root,0)
        return answer.values()
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = list( self.levelOrder(root))
        for i in range(1,len(levels),2):
            levels[i]  = levels[i][::-1]
        return levels
            