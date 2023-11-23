class Node :
    def __init__(self):
        self.val = None
        self.key = None
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def findNode(self,key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next
        return -1
    
    def addNode(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self,key):
        node = self.findNode(key)
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev


class MyHashMap:

    def __init__(self):
        self.dic = set()
        self.linkedList = LinkedList()

    def put(self, key: int, value: int) -> None:
        
        if key in self.dic:
            node = self.linkedList.findNode(key)
            node.val = value
        else:
            self.dic.add(key)
            newNode = Node()
            newNode.val = value
            newNode.key = key
            self.linkedList.addNode(newNode)

    def get(self, key: int) -> int:
        node = self.linkedList.findNode(key)
        if node != -1:
            return node.val
        return -1
        
    def remove(self, key: int) -> None:
        
        if key in self.dic:
            self.linkedList.removeNode(key)
            self.dic.remove(key)
        
        
       
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)