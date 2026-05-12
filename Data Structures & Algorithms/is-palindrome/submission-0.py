class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        filtered = ''.join(c for c in s if c.isalnum())
        return filtered==filtered[::-1]