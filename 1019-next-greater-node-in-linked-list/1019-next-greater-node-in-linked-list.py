# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stack = []

        while head:
            while stack and head.val > ans[stack[-1]]:
                index = stack.pop()
                ans[index] = head.val
            stack.append(len(ans))
            ans.append(head.val)
            head = head.next

        for i in stack:
            ans[i] = 0

        return ans