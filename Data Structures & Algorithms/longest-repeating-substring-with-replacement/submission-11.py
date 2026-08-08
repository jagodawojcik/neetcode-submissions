class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # condition, result: len(substr) - most_freq_char <= k

        freq_map = defaultdict(int)
        max_freq = 0
        res = 0
        l = 0

        for r in range(len(s)):
            freq_map[s[r]] += 1
            max_freq = max(max_freq, freq_map[s[r]])
            while (r - l + 1) - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
            
            res = max(res, (r-l+1))

        return res



