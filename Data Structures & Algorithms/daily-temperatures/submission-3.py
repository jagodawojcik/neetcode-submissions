class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # monotonically decreasing stack
        s = [] # indexes
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while s and temperatures[s[-1]] < t:
                res[s[-1]] = i - s[-1]
                s.pop()
            
            s.append(i)


        return res