# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr  = head
        
        if head == None:
            return None
        if k == 0 :
            return head
        
        while curr:
            length +=1
            curr = curr.next
        
        steps = k%length
        move = length - steps
       
        dummy1  = ListNode(0)
        dummy2  = ListNode(0)
        frontdum1 = dummy1
        frontdum2 = dummy2
        
        curr = head 
        while curr:
            if move > 0:
                frontdum1.next = curr
                frontdum1 = curr
            else:
                frontdum2.next = curr
                frontdum2 = curr
            move -=1
            curr = curr.next
        
        frontdum1.next = None
        frontdum2.next = dummy1.next
        return dummy2.next
                
            