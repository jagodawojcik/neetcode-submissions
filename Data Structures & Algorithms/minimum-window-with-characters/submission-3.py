class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        
        freq_t = {}
        for c in t:
            freq_t[c] = freq_t.get(c, 0) + 1
        
        min_substr = ""
        
        for l in range(len(s)):
            for r in range(l + len(t), len(s) + 1):
                substr = s[l:r]
                ok = True
                for key, val in freq_t.items():
                    if substr.count(key) < val:
                        ok = False
                        break
                if ok:
                    if min_substr == "" or len(substr) < len(min_substr):
                        min_substr = substr
                    break  # no need to extend r further
        
        return min_substr








