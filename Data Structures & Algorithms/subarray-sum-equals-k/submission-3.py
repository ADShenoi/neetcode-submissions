class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        mp = {0:1}
        count = 0
        for num in nums:
            prefix_sum += num
            diff = prefix_sum - k
            count += mp.get(diff, 0)
            mp[prefix_sum] = 1 + mp.get(prefix_sum, 0)
        
        return count
            