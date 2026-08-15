class Solution:
    def simplifyPath(self, path: str) -> s:


        res = [] # store individual dir/file names
        current = "" # current word


        for c in path + "/":
            if c == '/':
                if current == ".":
                    pass
                elif current == "..":
                    if res:
                        res.pop()
                else:
                    if current:
                        res.append(current)

                current = ""

            else:
                current += c

        return "/" + "/".join(res)