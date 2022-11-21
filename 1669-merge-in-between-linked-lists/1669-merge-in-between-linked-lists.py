# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        curr = list2
        len1 = 0
        while curr:
            curr,len1 = curr.next,len1+1
        
        curr = list2
        end1 = None
        while curr:
            if len1 == 1:
                end1 = curr
            curr,len1 = curr.next,len1-1
       
        b = b-a+1
        curr = list1
        temp  = None
        while curr:
            a -= 1
            if a == 0:
                temp = curr
                curr = curr.next
                temp.next =list2
                break
            curr = curr.next
      
        temp = None
        while curr:
            if b == 0:
                temp = curr
                break
            b-=1
            curr = curr.next
       
        end1.next = temp
        return list1