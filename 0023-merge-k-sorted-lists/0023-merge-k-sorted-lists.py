# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        for i in range(len(lists)):
            linked_list = lists[i]
            while linked_list:
                heappush(heap,linked_list.val)
                linked_list = linked_list.next
        
        dummy = ListNode(0)
        temp = dummy
        while heap:
            temp.next = ListNode(heappop(heap))
            temp = temp.next
          
        return dummy.next