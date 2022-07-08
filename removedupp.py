# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def deleteDuplicates(self, head):

        fake_head = ListNode(101, head)
        cur = fake_head
        front = head.next if head else None
        
        while cur.next:
            if front and cur.next.val == front.val:
                front = front.next
            elif cur.next.next == front:
                cur = cur.next
                front = front.next if front else None
            else:
                cur.next = front
                front = front.next if front else None
                
                
        return fake_head.next
