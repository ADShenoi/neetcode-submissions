class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            length = 0
            curr = num

            while curr in num_set:
                length += 1
                curr += 1
            
            longest = max(longest, length)
        
        return longest