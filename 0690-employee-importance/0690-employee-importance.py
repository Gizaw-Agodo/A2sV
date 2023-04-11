"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = defaultdict()
        for employee in employees :
            dic[employee.id] = employee
         
        visited = []
        self.total = 0
        def dfs(node):
            
            self.total += node.importance
            for id in node.subordinates :
                 dfs(dic[id])
        
        dfs(dic[id])
        return self.total