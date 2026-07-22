class Solution:

    def encode(self, strs: List[str]) -> str:

        # ["Hello","World"]
        # "Hello#World"
        # "5#Hello5#World"
        encoded = ""
        for string in strs:
            encoded += str(len(string))
            encoded += "#"
            encoded += string
        return encoded

    def decode(self, s: str) -> List[str]:
        
        decoded = []
        i = 0
        while i < len(s):
            word_len = ""
            while s[i] and s[i] != "#":
                word_len += s[i]
                i += 1

            decoded.append(s[i+1:i + int(word_len) + 1])
            i = i + int(word_len) + 1

        return decoded










