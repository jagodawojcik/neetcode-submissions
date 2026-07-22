class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = 0
        for i, c in enumerate(s):
            unique = set()
            substr = c
            unique.add(c)
            for j in range(i+1, len(s)):
                if s[j] not in unique:
                    substr += s[j]
                    print(substr)
                    unique.add(s[j])
                else:
                    break
            max_len = max(max_len, len(substr))
        
        return max_len