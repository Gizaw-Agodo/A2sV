# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        evenStart = head.next
        odd,even = head,head.next
        while odd and even and even.next:
            odd.next = even.next
            odd = odd.next
            
            if odd:
                even.next = odd.next
                even = even.next
        
        odd.next = evenStart
        return head
                
        
                
            
           