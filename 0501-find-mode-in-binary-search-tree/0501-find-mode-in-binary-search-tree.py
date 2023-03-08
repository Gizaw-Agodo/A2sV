# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        def countNodes(node):
            if node == None:
                return
            count[node.val] += 1
            countNodes(node.left)
            countNodes(node.right)
        countNodes(root)
        
        answer = []
        maximum = max(count.values())
        for key in count:
            if count[key] == maximum:
                answer.append(key)
        return answer
      