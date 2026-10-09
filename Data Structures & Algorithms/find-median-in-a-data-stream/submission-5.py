class MedianFinder:

    def __init__(self):
        self.numbers = []     

    def addNum(self, num: int) -> None:
        l, r = 0, len(self.numbers) - 1
        while l <= r: # log n
            m = (l + r) // 2
            if self.numbers[m] == num:
                l = m + 1
                break
            elif self.numbers[m] > num:
                r = m - 1
            else:
                l = m + 1

        self.numbers.insert(l, num) # n

        
    def findMedian(self) -> float:
        num_len = len(self.numbers)
        if num_len % 2 != 0:
            return float(self.numbers[num_len // 2])
        else:
            return float((self.numbers[num_len // 2 - 1] + self.numbers[num_len // 2]) / 2)
        
        