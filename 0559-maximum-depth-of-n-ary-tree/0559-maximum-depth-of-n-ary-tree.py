"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

    def maxDepth(self, root: 'Node') -> int:
        
        def findMax(root):
            
            child_max = 0
            if root != None:
                for child in root.children:
                    child_max =  max(findMax(child),child_max) 

                return child_max + 1
            return child_max
        return findMax(root)
        