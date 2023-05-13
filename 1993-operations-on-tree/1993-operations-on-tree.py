class LockingTree:

    def __init__(self, parent: List[int]):
        self.graph = defaultdict(list)
        self.parent = parent
        self.locked = {}
        
        for i in range(1,len(parent)):
            self.graph[parent[i]].append(i)
        

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked: return False 
        self.locked[num] = user
        return True 

    def unlock(self, num: int, user: int) -> bool:
        if self.locked.get(num) != user: return False 
        self.locked.pop(num)
        return True 

    def upgrade(self, num: int, user: int) -> bool:
        
        def checkAncestor(node):
            if  node in self.locked:
                return True
            elif node == -1:
                return False
            return checkAncestor(self.parent[node])
        
        def checkDescendant(node):
            for child in self.graph[node]:
                if child in self.locked:
                    return True
                if checkDescendant(child):
                    return True
            
            return False
        
        def unlockDescendants(node):
            
            for child in self.graph[node]:
                if child in self.locked:
                    self.locked.pop(child)
                    
                unlockDescendants(child)
        
        if num in self.locked: return False
        
        if checkAncestor(self.parent[num]): return False
        
        if not checkDescendant(num): return False
            
        unlockDescendants(num)
        self.locked[num] = user
        
        return True
        
        
            


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)