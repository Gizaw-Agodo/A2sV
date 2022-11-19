# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr :
            count +=1
            curr = curr.next
            
        curr = head
        position = 1
        while curr:
            if position == k:
                left  = curr
            if position == count-k+1:
                right = curr
            curr =curr.next
            position +=1
        left.val,right.val = right.val,left.val
        return head
            