class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        scores = []


        for n in operations:
            if n == "+":
                scores.append(scores[-1] + scores[-2])
            elif n == "C":
                scores.pop()
            elif n == "D":
                scores.append(scores[-1] *2)
            else:
                scores.append(int(n))

        return sum(scores)