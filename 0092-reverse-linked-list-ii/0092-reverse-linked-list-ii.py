# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right :
            return head
        temp = dummy = ListNode(0)
        dummy.next = head
        
        for i in range(left-1):
            temp = temp.next
      
       
        tail = temp.next
        for i in range(right-left):
            var = temp.next
            temp.next = tail.next
            tail.next = tail.next.next
            temp.next.next = var
        return dummy.next
       
        


       

