# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) :
        answer = defaultdict(list)
        
        def findLevel(root, level):
            if root == None:
                return 
            answer[level].append(root.val)
            findLevel(root.left, level + 1)
            findLevel(root.right, level + 1)
        
        findLevel(root,0)
        answer = list(answer.values())
       
        for i in range(1,len(answer),2):
            answer[i]  = answer[i][::-1]
        return answer
            