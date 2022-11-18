# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lDummy = ListNode(0)
        gDummy = ListNode(0)
        
        lFront ,gFront, curr = lDummy,gDummy,head
        
        while curr:
            if curr.val < x:
                lFront.next = curr
                lFront = curr
            else:
                gFront.next = curr
                gFront = curr
            curr = curr.next
        
        lFront.next = gDummy.next
        gFront.next = None
        
        return lDummy.next