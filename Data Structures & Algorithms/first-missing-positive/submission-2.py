class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1

        for i in range(1, max(nums)):
            if i not in d:
                return i
        
        if max(nums) < 0:
            return 1
        else:
            return max(nums)+1