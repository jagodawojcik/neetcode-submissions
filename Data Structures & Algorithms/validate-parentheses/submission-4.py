class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = {"(" : ")", "[" : "]", "{" : "}"}

        opening = []

        for b in s:
            if b in mapping:
                opening.append(b)
            else:
                if not opening:
                    return False
                
                if b == mapping[opening[-1]]:
                    opening.pop()
                else:
                    return False
        
        if opening:
            return False

        return True




        