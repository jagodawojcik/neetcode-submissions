class MinStack:

    def __init__(self):
        self.s = []
        self.min_s = []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.min_s and val > self.min_s[-1]:
            self.min_s.append(self.min_s[-1])
            return
        self.min_s.append(val)
            
        
    def pop(self) -> None:
        self.s.pop()
        self.min_s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        # O(n): min -> for n in self.s: update min, return min
        return self.min_s[-1]

