# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        node = temp
        while node.next is not None and node.next.next is not None:
            first = node.next
            second = node.next.next
            first.next = second.next
            node.next = second
            node.next.next = first
            node = node.next.next
        return temp.next