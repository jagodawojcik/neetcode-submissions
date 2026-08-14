class Solution:
    def simplifyPath(self, path: str) -> str:
        
        if path == "/":
            return "/"

        res = []
        word = ""
        # neetcode/practice/
        # path="/neetcode/practice//...///../courses"
        for c in path + '/':
            if c == '/':
                if word == "..":
                    if res:
                        res.pop()
                elif word and word != '.':
                    res.append(word)
                word = ""
            else:
                word += c
        
        return "/" + "/".join(res)


        