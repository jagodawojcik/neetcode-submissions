class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # k = allowed replacements
        # max_substr => len(subtr) - most_freq_c <= k

        freq_c = defaultdict(int)
        res = 0
        l, r = 0, 0
        
        while r < len(s):
            freq_c[s[r]] += 1
            if (r - l + 1) - max(freq_c.values()) <= k:
                res = max(res, (r - l + 1))
            else:
                freq_c[s[l]] -= 1
                l += 1
            r += 1


        return res



