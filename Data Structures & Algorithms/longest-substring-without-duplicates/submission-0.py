class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        i, j = 0, 0
        count = 0
        while j < len(s):
            while s[j] in s[i:j]:
                i += 1
            j += 1
            count = max(count, j-i)
        return count
        