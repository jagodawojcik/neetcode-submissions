class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_substr_len = 0
        for i in range(len(s)):
            freq_map = {}
            for j in range(i, len(s)):
                freq_map[s[j]] = freq_map.get(s[j], 0) + 1
                max_freq = max(freq_map.values())
                replacement_sum = sum(freq_map.values()) - max_freq

                if replacement_sum > k:
                    break
                max_substr_len = max(max_substr_len, len(s[i:j+1]))
        return max_substr_len






