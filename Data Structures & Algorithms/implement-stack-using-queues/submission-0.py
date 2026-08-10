class MyStack:

    def __init__(self):
        self.stack = deque()

        
    def push(self, x: int) -> None:
        self.stack.append(x) # O(1)
        

    def pop(self) -> int:
        for i in range(len(self.stack) - 1):
            self.push(self.stack.popleft())
            # popping from the left which is allowed except for last el
            # and appending it back to the right

        return self.stack.popleft()

        

    def top(self) -> int:
        return self.stack[-1] # O(n)
        

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()