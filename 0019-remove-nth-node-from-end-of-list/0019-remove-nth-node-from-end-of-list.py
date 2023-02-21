# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # finding the count of the linked list      
        count = 0
        temp = head
        while temp :
            count += 1
            temp = temp.next
            
        # finding target index
        index = count - n
        
        dummy = ListNode(0)
        dummy.next = head
        
        temp = dummy
        while index  :
            temp = temp.next
            index-=1
        temp.next = temp.next.next
        return dummy.next