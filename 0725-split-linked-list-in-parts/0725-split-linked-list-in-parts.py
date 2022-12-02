# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        answer = []
        count = 0
        temp = head 
        while temp :
            count +=1
            temp = temp.next
        
        dividend,rem = count//k , count %k
      
        while head :
            currCount = dividend 
            if rem > 0:
                currCount +=1
                rem -=1
            answer.append(head)
            for i in range(currCount-1):
                head = head.next
            
            if not head :break
            temp = head.next
            head.next = None
            head = temp

        while  len(answer) < k:
            answer.append(None)
        return answer
    
            
            
            
            
            
            
            
            
            
            