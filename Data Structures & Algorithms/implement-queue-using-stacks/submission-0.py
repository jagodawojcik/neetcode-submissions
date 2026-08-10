class MyQueue:

    def __init__(self):
        self.queue = []
        self.tmp_storage = []
        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        el = self.queue[0]
        for i in range(1, len(self.queue)):
            self.tmp_storage.append(self.queue[i])

        self.queue = self.tmp_storage[:]
        self.tmp_storage = []

        return el
        

    def peek(self) -> int:
        return self.queue[0]
        
    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()