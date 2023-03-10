# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 == None :
            return list2
        elif list2 == None:
            return list1
        if list1.val <= list2.val :
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
    
    def divide(self, node):
        slow = node
        fast = node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        return temp
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        slow = self.divide(head)
        list1 = self.sortList(head)
        list2 = self.sortList(slow)
        return(self.mergeTwoLists(list1, list2))
         
        
            
        
        
        
        
        
        
        
     
    
    
    
    
    
                
