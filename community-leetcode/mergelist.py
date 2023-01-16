# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1.val < list2.val :
            temp = list1
        else:
            temp = list2
        
        var = temp.next
        


        while list1!= None and list2 != None:
            if list1.val < list2.val:
                var = list1
                var.next = list2
                var = var.next

                list1 = list1.next
                list2 = list2.next
            else:
                var = list2 
                var.next = list1
                var = var.next
                list1 = list1.next
                list2 = list2.next

        return temp 
