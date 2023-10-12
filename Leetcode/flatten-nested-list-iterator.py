# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.index = 0
        self.flattend = []
        def dp(array):
            for element in array:
                if element.isInteger():
                    self.flattend.append(element.getInteger())
                else:
                    dp(element.getList())   
        dp(nestedList)
       
    def next(self) -> int:
        currElement =  self.flattend[self.index]
        self.index += 1
        return currElement
    
    def hasNext(self) -> bool:
        if self.index < len(self.flattend):
            return  True
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
