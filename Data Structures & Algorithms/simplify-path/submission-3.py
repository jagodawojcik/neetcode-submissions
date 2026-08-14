class Solution:
    def simplifyPath(self, path: str) -> str:
        
        if path == "/":
            return "/"

        result = []
        word = ""
        for c in path:
            if c == "/":
                if not word:
                    continue
                
                if word == "..":
                    if result:
                        result.pop()
                elif word == ".":
                    pass
                else:    
                    result.append(word)
                word = ""
            else:
                word += c
        
        if word == "..":
            if result:
                result.pop()
        elif word == ".":
            pass
        elif word:    
            result.append(word)

        return "/" + "/".join(result)
















        
        res = []
        for c in path:
            if res and c == '/':
                dots_count = 0
                while res and res[-1] == '/':
                    res.pop()
                while res and res[-1] == '.':
                    dots_count += 1
                    res.pop()
                if dots_count == 0:
                    pass
                elif dots_count == 1:
                    res.pop() # remove extra slash
                elif dots_count == 2:
                    res.pop() # remove extra slash
                    while res and res[-1] != '/':
                        res.pop()
                    if res:
                        res.pop() # remove extra slash
                else:
                    for i in range(dots_count):
                        res.append('.')
                
                
            res.append(c)

        if len(res) > 1 and res[-1] == '/':
            res.pop()

        output = ""
        for n in res:
            output += n

        return output