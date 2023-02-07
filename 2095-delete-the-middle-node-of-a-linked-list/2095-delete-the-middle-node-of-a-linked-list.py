# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        middle = length//2 + 1
        
        dummy  = ListNode(0)
        dummy.next = head
        temp2  = dummy
        index = 0
        while temp2: 
            index += 1
            if index == middle:
                temp2.next = temp2.next.next
            temp2 = temp2.next    
        return dummy.next
                
            
            
        
        