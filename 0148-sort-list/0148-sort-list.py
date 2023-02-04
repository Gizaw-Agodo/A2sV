# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_list = []
        while head:
            temp_list.append(head.val)
            head = head.next
        
        temp_list.sort()
        dummy_node = ListNode(0)
        temp = dummy_node
        for val in temp_list:
            new_node = ListNode(val)
            temp.next = new_node
            temp = new_node
            
        return dummy_node.next