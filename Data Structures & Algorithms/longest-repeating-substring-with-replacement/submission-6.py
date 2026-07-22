class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_substr_len = 0
        l, r = 0, 0 

        freq_map = {}
        while r < len(s):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            max_freq = max(freq_map.values())

            while (r - l + 1) - max_freq > k and l < r:
                freq_map[s[l]] -= 1
                l += 1

            max_substr_len = max(max_substr_len, len(s[l:r+1]))
            r += 1

        return max_substr_len






