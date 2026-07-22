class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        freq_map_t = {}
        for c in t:
            freq_map_t[c] = freq_map_t.get(c, 0) + 1
        
        min_sub = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                flag = True
                for key, val in freq_map_t.items():
                    if s[i:j+1].count(key) < val:
                        flag = False
                        break
                if flag == True:
                    if (j - i + 1) < len(min_sub) or min_sub == "":
                        min_sub = s[i:j+1]
                    break
    
        return min_sub








