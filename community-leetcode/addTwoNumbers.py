# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = ListNode()
        tempNode = node
        rem = 0
        while (l1 != None or l2 != None ):
            if l1 !=None and l2!=None:
                temp = l1.val + l2.val + rem
                rem = 0
                l1= l1.next
                l2 = l2.next
                if temp > 9:
                    # mylist.append(temp%10)
                    tempNode.next = ListNode(temp%10)
                    rem = temp/10
                else:tempNode.next = ListNode(temp)
            if l1 == None and l2 != None:
                temp = l1.val + rem
                rem = 0
                l2 = l2.next
                if temp > 9:
                    # mylist.append(temp%10)
                    tempNode.next = ListNode(temp%10)
                    rem = temp/10
                else:tempNode.next = ListNode(temp)

            if l1 != None and l2 == None:
                temp = l1.val + rem
                rem = 0
                l1 = l1.next
                if temp > 9:
                    tempNode.next = ListNode(temp%10)
                    rem = temp/10
                else:tempNode.next = ListNode(temp)
        if rem !=0 :
            tempNode.next = ListNode(rem)
            
        
        
        return node
