class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        min_len = float('inf')
        l, r = 0, 0

        while l <= r and r < len(nums):
            total += nums[r]

            if total >= target:
                while l <= r and total >= target:
                    min_len = min(min_len, r-l+1)
                    total -= nums[l]
                    l += 1
            r += 1
        return 0 if min_len == float('inf') else min_len