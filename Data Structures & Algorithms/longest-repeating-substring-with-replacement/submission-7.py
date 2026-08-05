class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # allowed replacements = len(window) - highest freq character
        # allowed replacements <= k

        max_len = 0
        l = 0
        freq_map = defaultdict(int)

        for r in range(len(s)):
            freq_map[s[r]] += 1
            while (r - l + 1) - max(freq_map.values()) > k:
                freq_map[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len

        

