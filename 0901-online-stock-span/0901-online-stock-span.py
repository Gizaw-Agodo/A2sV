class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []
    def next(self, price: int) -> int:
        curr_value = 1
        while self.stack and self.prices[-1] <= price:
            value = self.stack.pop()
            self.prices.pop()
            curr_value += value
            
        self.stack.append(curr_value)
        self.prices.append(price)
        return self.stack[-1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)