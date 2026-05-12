class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        longest = 0

        i = 0
        while i < len(nums):
            length = 0
            curr = nums[i]

            while curr in nums:
                length += 1
                curr += 1
            
            i += 1
            
            longest = max(longest, length)
        
        return longest

