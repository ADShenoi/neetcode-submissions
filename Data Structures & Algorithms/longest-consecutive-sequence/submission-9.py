class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        nums.sort()
        longest = 0

        for i in range(len(nums)-1):
            length = 0
            curr = nums[i]

            while curr in nums:
                length += 1
                curr += 1
            
            longest = max(longest, length)
        
        return longest

