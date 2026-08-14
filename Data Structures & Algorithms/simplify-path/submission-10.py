class Solution:
    def simplifyPath(self, path: str) -> str:
        
        if path == "/":
            return "/"

        words = path.split('/')
        stack = []


        for w in words:
            if w == "..":
                if stack:
                    stack.pop()
            elif w and w != ".":
                stack.append(w)
            
        
        return "/" + "/".join(stack)


        