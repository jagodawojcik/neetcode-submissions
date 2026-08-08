class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # condition, result: len(substr) - most_freq_char <= k

        freq_map = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):
            freq_map[s[r]] += 1
            while (r - l + 1) - max(freq_map.values()) > k:
                freq_map[s[l]] -= 1
                l += 1
            
            res = max(res, (r-l+1))

        return res



