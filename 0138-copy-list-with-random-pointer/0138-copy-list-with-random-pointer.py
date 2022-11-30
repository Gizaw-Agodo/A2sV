"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dic = {}
        dummy = Node(0)
        curr,copy = head,dummy
        
        while curr:
            copy.next = Node(curr.val)
            dic[curr] = copy.next
            curr = curr.next
            copy = copy.next
        
        curr,copy = head,dummy.next
        while curr:
            copy.random = dic[curr.random] if curr.random else None
            curr = curr.next
            copy = copy.next
        return dummy.next

    