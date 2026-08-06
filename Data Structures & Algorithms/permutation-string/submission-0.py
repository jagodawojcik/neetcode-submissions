class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need_chars = defaultdict(int)
        for c in s1:
            need_chars[c] += 1

        window = defaultdict(int)
        for i in range(len(s1)):
            window[s2[i]] += 1

        if window == need_chars:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            # remove left character
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]

            # add right character
            window[s2[r]] += 1

            # check if window is a permutation of s1
            if window == need_chars:
                return True
            l += 1

        return False