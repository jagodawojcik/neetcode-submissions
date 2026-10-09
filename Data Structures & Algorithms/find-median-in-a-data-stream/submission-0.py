class MedianFinder:

    def __init__(self):
        self.numbers = []     

    def addNum(self, num: int) -> None:
        self.numbers.append(num)
        self.numbers.sort() # nlog(n)
        
    def findMedian(self) -> float:
        num_len = len(self.numbers)
        if num_len % 2 != 0:
            return float(self.numbers[num_len // 2])
        else:
            return float((self.numbers[num_len // 2 - 1] + self.numbers[num_len // 2]) / 2)
        
        