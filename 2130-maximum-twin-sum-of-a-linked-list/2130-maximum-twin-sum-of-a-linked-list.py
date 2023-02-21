# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mylist = []
        while head :
            mylist.append(head.val)
            head = head.next
        initial = 0
        final = len(mylist)-1
        answer = 0 
        while initial < final :
            answer = max(answer, mylist[initial]+mylist[final])
            initial +=1
            final -=1
        return answer