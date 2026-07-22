class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        unique_chars = set()
        max_len = 0
        l, r = 0, 0
        while r < len(s):
            while s[r] in unique_chars and l < r:
                unique_chars.remove(s[l])
                l += 1
            unique_chars.add(s[r])
            r += 1
            max_len = max(len(unique_chars), max_len)

        # for i in range(len(s)):
        #     unique_chars = set()
        #     for j in range(i, len(s)):
        #         if s[j] in unique_chars:
        #             break
        #         unique_chars.add(s[j])
        #     max_len = max(max_len, len(unique_chars))

        return max_len
        