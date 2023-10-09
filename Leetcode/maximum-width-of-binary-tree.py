# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(list)
        dic[0] = [1]

        def dfs(root, parentVal, level):
            if root is None:
                return 

            if root.left:
                currVal = (parentVal - 1)*2 + 1
                dic[level].append(currVal)
                dfs(root.left, currVal, level + 1)
                
            if root.right:
                currVal = (parentVal - 1)*2 + 2
                dic[level].append(currVal)
                dfs (root.right, currVal , level + 1)
        
        dfs(root, 1, 1)
       
        maxValue = float('-inf')
        for value in dic.values():
            currValue = value[-1] - value[0] + 1
            maxValue = max(maxValue, currValue)
        return maxValue



        
