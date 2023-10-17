class RandomizedSet:

    def __init__(self):
        self.dic = defaultdict(int)
        
    def insert(self, val: int) -> bool:

        if self.dic[val] == 1:
            return False
        
        self.dic[val] = 1
        return True
        
    def remove(self, val: int) -> bool:
        
        if self.dic[val] == 0:
            self.dic.pop(val)
            return False

        self.dic.pop(val)
        return True
        
    def getRandom(self) -> int:
        return random.choice(list(self.dic.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
