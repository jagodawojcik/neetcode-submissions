class StockSpanner:

    def __init__(self):
        self.span = [] # (stock, span), monotonically decreasing, don't need to keep   all vals
        

    def next(self, price: int) -> int:
        span = 1
        while self.span and self.span[-1][0] <= price:
            span += self.span[-1][1]
            self.span.pop()

        self.span.append((price, span))

        return self.span[-1][1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)