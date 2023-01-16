class Node:
    
    def __init__(self, key, val, next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class CustomStack:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0, prev = self.head)
        self.head.next = self.tail
    
    def addLast(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def removeFirst(self):
        if self.head.next == self.tail:
            return None
        node = self.head.next
        self.remove(node)
        return node
        
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.stack = CustomStack()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            temp = self.dic[key]
            self.stack.remove(temp)
            self.stack.addLast(temp)
            return temp.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.stack.remove(node)
            self.stack.addLast(node)
        elif self.capacity:
            node = Node(key,value)
            self.dic[key] = node
            self.capacity -= 1
            self.stack.addLast(node)
        else:
            node = self.stack.removeFirst()
            self.dic.pop(node.key)
            self.dic[key] = Node(key, value)
            self.stack.addLast(self.dic[key])

