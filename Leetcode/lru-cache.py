class Node:
    def __init__(self):
        self.key = None
        self.val = None
        self.prev = None
        self.next = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # addNone to linked list
    def addNode(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # remove node
    def removeNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    # move to head
    def moveToHead(self, node):
        self.removeNode(node)
        self.addNode(node)
    
    # poptail 
    def popTail(self):
        prev = self.tail.prev
        self.removeNode(prev)
        return prev
    

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.count = 0
        self.capacity = capacity
        self.linkedList = DoublyLinkedList()

    def get(self, key: int) -> int:
        
        if key in self.cache :
            node = self.cache[key]
            self.linkedList.moveToHead(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.linkedList.moveToHead(node)
        else:
            newNode = Node()
            newNode.key = key
            newNode.val = value
            self.cache[key] = newNode
            self.linkedList.addNode(newNode)
            self.count += 1 

            if self.count > self.capacity:
                tail = self.linkedList.popTail()
                del self.cache[tail.key]
                self.count -= 1


    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
