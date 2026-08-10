class MyQueue:

    def __init__(self):
        self.queue = []
        self.tmp_storage = []
        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        while len(self.queue) > 1:
            self.tmp_storage.append(self.queue.pop())
        el = self.queue.pop()

        while self.tmp_storage:
            self.queue.append(self.tmp_storage.pop())
        return el
        

    def peek(self) -> int:

        while len(self.queue) > 1:
            self.tmp_storage.append(self.queue.pop())
        el = self.queue.pop()
        self.tmp_storage.append(el)
        while self.tmp_storage:
            self.queue.append(self.tmp_storage.pop())
        return el
        
        
    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()