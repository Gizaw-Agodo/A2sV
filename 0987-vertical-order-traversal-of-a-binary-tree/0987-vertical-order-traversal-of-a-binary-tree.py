# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        positions = defaultdict(list)
        def findPosition(node,curr_pos,level):
            if node == None:
                return 
            positions[node] = [curr_pos,level]
            findPosition(node.left,[curr_pos[0] + 1,curr_pos[1]-1],level+1)
            findPosition(node.right,[curr_pos[0] + 1,curr_pos[1]+1],level+1)
        
        findPosition(root,[0,0],0)
        pos_list = [[i,positions[i]] for i in positions]
        pos_list.sort(key = lambda x :(x[1][0][1], x[1][1],x[0].val))
        answer_dic = defaultdict(list)
        for val in pos_list:
            answer_dic[val[1][0][1]].append(val[0].val)
        return answer_dic.values()
