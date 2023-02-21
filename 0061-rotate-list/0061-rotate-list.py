# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       
        if head == None:
            return None

        # finding the length of linked list and last node
        length = 1
        last_node = head
        while last_node.next:
            length += 1
            last_node = last_node.next
        
        # determing the kth node
        k = k % length
        steps = length - k -1 
        dummy_node = head 
        while steps > 0:
            dummy_node  = dummy_node.next
            steps -= 1
            
        last_node.next = head
        answer = dummy_node.next
        dummy_node.next = None
        
        return answer
       
      
        
        
        