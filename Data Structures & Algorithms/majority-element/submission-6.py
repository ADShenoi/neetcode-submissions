class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}

        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        return max(counter, key=lambda k:counter[k])