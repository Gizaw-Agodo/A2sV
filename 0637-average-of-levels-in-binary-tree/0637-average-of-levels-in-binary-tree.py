# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        answer = defaultdict(list)
        def findLevel(root, level):
            if root == None:
                return 
            answer[level].append(root.val)
            findLevel(root.left, level + 1)
            findLevel(root.right, level + 1)
        
        findLevel(root,0)
        return [sum(items)/len(items) for items in answer.values()]