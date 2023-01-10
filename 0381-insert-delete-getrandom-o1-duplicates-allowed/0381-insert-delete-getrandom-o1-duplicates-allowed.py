class RandomizedCollection:

    def __init__(self):
        self.random_collection = []
        
    def insert(self, val: int) -> bool:
        col = self.random_collection
        set_collection = set(col)
        if val in set_collection:
            self.random_collection.append(val)
            return False
        else:
            self.random_collection.append(val)
            return True
            

    def remove(self, val: int) -> bool:
        set_collection = set(self.random_collection)
        if val in set_collection:
            self.random_collection.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        num =  random.choice(self.random_collection)
        return num
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()