class MyQueue:

    def __init__(self):
        self.q = [] # push to this q
        self.q2 = [] # peek/pop to this q
        

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        if not self.q2:
            while self.q:
                self.q2.append(self.q.pop())

        return self.q2.pop()
        

    def peek(self) -> int:
        if not self.q2:
            while self.q:
                self.q2.append(self.q.pop())
        
        return self.q2[-1]
        

    def empty(self) -> bool:
        return len(self.q) == 0 and len(self.q2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()