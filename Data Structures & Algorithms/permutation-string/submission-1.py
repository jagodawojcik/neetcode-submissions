class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need_chars = [0] * 26
        for c in s1:
            need_chars[ord(c) - ord('a')] += 1

        window = [0] * 26
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1

        if window == need_chars:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            # remove left character
            window[ord(s2[l]) - ord('a')] -= 1

            # add right character
            window[ord(s2[r]) - ord('a')] += 1

            # check if window is a permutation of s1
            if window == need_chars:
                return True
            l += 1

        return False