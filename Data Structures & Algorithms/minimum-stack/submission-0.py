class MinStack:

    def __init__(self):
        self.stack = [] # 1, 2, 0
        self.min_vals_stack = [] # 1,  1, 
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_vals_stack:
            self.min_vals_stack.append(val)
            return None
        
        if val < self.min_vals_stack[-1]:
            self.min_vals_stack.append(val)
            return None
        self.min_vals_stack.append(self.min_vals_stack[-1])
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_vals_stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_vals_stack[-1]

        
