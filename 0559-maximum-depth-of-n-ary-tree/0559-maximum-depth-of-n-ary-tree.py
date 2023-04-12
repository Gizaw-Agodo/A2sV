"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

    def maxDepth(self, root: 'Node') -> int:
        def findMax(maximum, root):
            if not root:
                return maximum
         
            maxx = maximum + 1
            for child in root.children:
                maxx =  max(findMax(maximum + 1, child),maxx)   
            return maxx
        return findMax(0, root)
        