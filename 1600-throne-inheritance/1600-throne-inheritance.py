class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.family = defaultdict(list)
        self.deaths = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.family[parentName].append(childName)
    

    def death(self, name: str) -> None:
        self.deaths.add(name)
    
    def getInheritanceOrder(self) -> List[str]:
        order = []
        def successor(parent) :
            if parent not in self.deaths:
                order.append(parent)
            for child in self.family[parent]:
                successor(child)

        successor(self.kingName)
       
        return order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()