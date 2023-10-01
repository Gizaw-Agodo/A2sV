class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.sum = 0


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.dic = defaultdict(int)
        
    def insert(self, key: str, val: int) -> None:
        curr = self.root
        diff = val - self.dic[key]

        for char in key:
            index = ord(char) - ord('a')
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr.children[index].sum += diff
            curr = curr.children[index]
        self.dic[key] = val


    def sum(self, prefix: str) -> int:
        curr = self.root
        for letter in prefix:
            index = ord(letter) - ord('a')
            if curr != None:
                curr = curr.children[index] 
        return curr.sum if curr != None else 0

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
