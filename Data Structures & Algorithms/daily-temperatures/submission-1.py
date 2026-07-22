class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                print(stack[-1])
                temp, outp_inx = stack.pop()
                result[outp_inx] = i - outp_inx
            stack.append((t, i))

        return result



