class MinStack:

    def __init__(self):
        self.s = [] # [2, 4, 1, 10, 0]
        self.s2 = [] # history of min values [2, 2, 1, 1, 0]

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.s2:
            if val < self.s2[-1]:
                self.s2.append(val)
            else:
                self.s2.append(self.s2[-1])
        else:
            self.s2.append(val)
            

    def pop(self) -> None:
        self.s.pop()
        self.s2.pop()

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.s2[-1]
        
