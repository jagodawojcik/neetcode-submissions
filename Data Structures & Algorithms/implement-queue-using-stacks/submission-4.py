class MyQueue:

    def __init__(self):
        self.q = []
        self.q2 = []
        

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        while self.q:
            self.q2.append(self.q.pop())
        
        res = self.q2.pop()

        while self.q2:
            self.q.append(self.q2.pop())

        return res
        

    def peek(self) -> int:
        while self.q:
            self.q2.append(self.q.pop())
        
        res = self.q2[-1]

        while self.q2:
            self.q.append(self.q2.pop())

        return res
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()