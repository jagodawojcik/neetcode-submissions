class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(c.lower() for c in s if c.isalnum())
        if new == new[::-1]:
            return True
        return False
