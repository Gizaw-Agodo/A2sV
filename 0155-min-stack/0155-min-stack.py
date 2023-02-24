class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            if self.minstack[-1] >= val:
                self.minstack.append(val)
        else:
            self.minstack.append(val)
        

    def pop(self) -> None:
        poped  = self.stack.pop()
        if poped == self.minstack[-1]:
            self.minstack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()