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
        count_list = [(i,count[i]) for i in count ]
        count_list.sort(key = lambda x: x[1], reverse = True)
        answer = []
        firstMax = count_list[0][1]
        for key,value in count_list:
            if value == firstMax:
                answer.append(key)
            else:
                break
        return answer