class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        lst = []

        for key, val in counter.items():
            if val > len(nums)/3:
                lst.append(key)
        
        return lst