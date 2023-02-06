# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
     
        dummy1 =  ListNode(0)
        dummy = dummy1
        temp = head
        segment_sum = 0
        
        while temp.next:
            if temp.next.val == 0:
                new_node = ListNode(segment_sum)
                dummy.next = new_node
                dummy = dummy.next
                segment_sum = 0
            else:
                segment_sum += temp.next.val
            temp = temp.next
            
        return dummy1.next