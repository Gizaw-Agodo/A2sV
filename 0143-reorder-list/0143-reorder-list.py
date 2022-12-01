# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow= fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow.next
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr  = nextNode
        slow.next = None
        
        curr = head 
        while curr and prev:
            leftNext = curr.next
            curr.next = prev
            rightNext = prev.next
            prev.next = leftNext
            curr = leftNext
            prev = rightNext
        
        
 
            