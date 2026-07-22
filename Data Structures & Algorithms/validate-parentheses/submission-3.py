class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = {"(" : ")", "[" : "]", "{" : "}"}

        opening_stack = []
        for c in s:
            if c in mapping: # if it's an opening bracket
                opening_stack.append(c)
            if c in list(mapping.values()): # if it's an closing bracket
                if not opening_stack:
                    return False
                opening = opening_stack.pop()
                if mapping[opening] == c:
                    continue
                else:
                    return False
        
        if opening_stack:
            return False
        return True



        