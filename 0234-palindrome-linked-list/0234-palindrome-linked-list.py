# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp_list = []
        prev  = None
        curr = head 
        
        while curr : 
            temp_list.append(curr.val)
            next  = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        for i in range(len(temp_list)):
            if prev.val != temp_list[i]:
                return False
            prev = prev.next
        return True
        