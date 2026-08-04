class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0

        unique_chars = set()
        max_len = 0
        while r < len(s):
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l += 1

            unique_chars.add(s[r])
            max_len = max(max_len, len(unique_chars))
            r += 1

        return max_len



