class Solution:

    def encode(self, strs: List[str]) -> str:
        #["hello", "world"]
        #["5#hello5#world"]
        encoded = ""
        for s in strs:
            encoded += str(len(s))
            encoded += "#"
            encoded += s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        #["512#hell..o512#world"]
        decoded = []

        i, j = 0, 0
        while i < len(s):
            if s[j] == "#":
                word_len = int(s[i:j])
                decoded.append(s[j+1:j+1+word_len])
                i = j+1+word_len
                j = i

            j += 1

        return decoded










