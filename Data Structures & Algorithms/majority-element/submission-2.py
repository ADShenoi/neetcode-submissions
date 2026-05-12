class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)

        return max(counter.keys(), key=lambda k: counter[k])