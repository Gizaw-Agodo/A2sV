# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        preve = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = preve
            preve = curr
            curr = next_node
        return preve
            
            