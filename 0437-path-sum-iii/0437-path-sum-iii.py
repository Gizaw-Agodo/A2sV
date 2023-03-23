# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = defaultdict(int)
        dic[0] += 1
        count = 0
        def findCount(root, temp_sum ):
            nonlocal count
            if root == None:
                return 
            temp_sum += root.val
            diff = temp_sum - targetSum
            count += dic[diff]
            dic[temp_sum] += 1
            findCount(root.left,temp_sum)
            findCount(root.right, temp_sum)
            dic[temp_sum] -= 1
            
        findCount(root, 0)
        return count