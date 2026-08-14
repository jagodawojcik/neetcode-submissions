class Solution:
    def simplifyPath(self, path: str) -> str:
        
        if path == "/":
            return "/"

        res = []
        word = ""
        # neetcode/practice/
        # path="/neetcode/practice//...///../courses"
        for c in path:
            if c == '/':
                if word == "..":
                    if res:
                        res.pop()
                elif word == ".":
                    pass
                else:
                    if word:
                        res.append(word)
                word = ""
            else:
                word += c
        
        if word:
            if word == "..":
                res.pop()
            elif word == ".":
                pass
            else:
                if word:
                    res.append(word)

        return "/" + "/".join(res)


        