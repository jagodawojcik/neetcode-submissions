class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # tokens=["3","*"]
        res = []

        for c in tokens:
            if c == "+":
                res.append(res.pop() + res.pop())
            elif c == "*":
                res.append(res.pop() * res.pop())
            elif c == "-":
                a = res.pop()
                b = res.pop()
                res.append(b - a)
            elif c == "/":
                a = res.pop()
                b = res.pop()
                res.append(int(b / a))
            else:
                res.append(int(c))
        return res[0]

