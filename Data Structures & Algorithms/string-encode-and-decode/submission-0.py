class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        
        for s in strs:
            encoded_str += str(len(s))
            encoded_str += '#'
            encoded_str += s

        return encoded_str


    # [4#neet4#code4#love4#you]

    def decode(self, s: str) -> List[str]:

        decoded_str = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])
            decoded_str.append(s[j+1 : j+1+word_len])
            i = j + word_len + 1
        return decoded_str









