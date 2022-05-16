# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        p = curr = dummy
        while n > 0:
            p = p.next
            n -= 1
        while p.next:
            p = p.next
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next
