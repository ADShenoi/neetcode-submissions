class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        l, r = 0, 0
        max_len = 0
        res = 0
        while r < len(s):
            d[s[r]] += 1
            max_len = max(max_len, d[s[r]])

            while ((r-l+1) - max_len) > k:
                d[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
            r += 1
        
        return res