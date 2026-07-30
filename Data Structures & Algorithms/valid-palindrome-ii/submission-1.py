class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s: str):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if not isPalindrome(s[l+1:r+1]) and not isPalindrome(s[l:r]):
                    return False
                else:
                    True
            l += 1
            r -= 1

        return True