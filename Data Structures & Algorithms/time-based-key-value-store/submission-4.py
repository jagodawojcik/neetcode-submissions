class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # key: [(timestamp, value)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        # sorted by default, every time we insert t2 >= t1


    def get(self, key: str, timestamp: int) -> str:
        # value_timestamp <= timestamp
        # O(n) -> O(logn)

        if key not in self.store:
            return ""
        
        values = self.store[key]
        l, r = 0, len(values) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2

            if values[m][0] == timestamp:
                return values[m][1]
            elif values[m][0] > timestamp:
                r = m - 1
            else:
                res = values[m][1]
                l = m + 1

        # for time, val in values:
        #     if time > timestamp:
        #         continue
        #     else:
        #         if res[0] < time:
        #             res = (time, val)
                
        return res

            