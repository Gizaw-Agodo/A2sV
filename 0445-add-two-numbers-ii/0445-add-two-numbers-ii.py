# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1digits = ""
        l2digits = ""
        head1 = l1
        while head1:
            l1digits += str(head1.val)
            head1 = head1.next
        head2 = l2
        while head2:
            l2digits += str(head2.val)
            head2 = head2.next
        total = int(l1digits) + int(l2digits)
        
        node = ListNode(0)
        dummy = node
        for val in str(total):
            temp = ListNode(int(val))
            dummy.next = temp
            dummy = temp
        return node.next
            