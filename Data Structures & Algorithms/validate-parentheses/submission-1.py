class Solution:
    def isValid(self, s: str) -> bool:
        

        stack = []
        # mapping = {")":"(", "]":"[", "}":"{"}
        mapping = {"(":")", "[":"]", "{":"}"}


        for b in s:
            if b in mapping:
                stack.append(b)
            else:
                if stack and mapping[stack[-1]] == b:
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        return True 
        