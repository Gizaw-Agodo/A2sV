# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None :
            return None 
        
        count = 0 
        head1 = head 
        while head1 != None:
            count +=1
            head1 = head1.next
        
        middle = count//2 +1
        head2 = head 
        for i in range(1,middle):
            head2  = head2.next 
        return head2
            
