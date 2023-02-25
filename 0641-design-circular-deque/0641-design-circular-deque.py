class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = deque()
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.appendleft(value)
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.queue):
            self.queue.popleft()
            return True
        return False
            

    def deleteLast(self) -> bool:
         if len(self.queue):
            self.queue.pop()
            return True
         return False

    def getFront(self) -> int:
         if len(self.queue):
            return self.queue[0]
         return -1
        

    def getRear(self) -> int:
         if len(self.queue):
            return self.queue[-1]
         return -1

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()