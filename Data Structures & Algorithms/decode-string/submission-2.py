class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        for c in s:
            if c == "]":
                substr = ""
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr

                print(substr)
                
                stack.pop() # remove '['
                
                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier

                for i in range(int(multiplier)):
                    stack.append(substr)

            else:
                stack.append(c)

        return "".join(stack)