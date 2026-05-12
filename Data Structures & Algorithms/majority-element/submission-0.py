class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)

        largest_k = 0
        largest_v = 0
        for k, v in counter.items():
            if v > largest_v:
                largest_v = v
                largest_k = k
        return largest_k