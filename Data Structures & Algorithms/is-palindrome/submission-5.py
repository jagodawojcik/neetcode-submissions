class Solution:
    def isPalindrome(self, s: str) -> bool:


        def isalphnum(c: str) -> bool:
            return ( 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9')

        l, r = 0, len(s) - 1

        while l < r:
            while not isalphnum(s[l]) and l < r:
                l += 1
            while not isalphnum(s[r]) and l < r:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1 


        return True
