class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        if t == "":
            return ""

        freq_map_t = defaultdict(int)
        for c in t:
            freq_map_t[c] += 1
        
        count_t = len(freq_map_t)
        found = 0
        
        min_sub = ""
        freq_map_s = defaultdict(int)
        l = 0
        for r in range(len(s)):
            if s[r] in freq_map_t:
                freq_map_s[s[r]] += 1

            if s[r] in freq_map_t and freq_map_s[s[r]] == freq_map_t[s[r]]:
                found += 1

            while found == count_t:
                if min_sub == "" or (r - l + 1) < len(min_sub):
                    min_sub = s[l:r+1]
                
                freq_map_s[s[l]] -= 1
                if s[l] in freq_map_t and freq_map_s[s[l]] < freq_map_t[s[l]]:
                    found -= 1
                l += 1
            
        return min_sub