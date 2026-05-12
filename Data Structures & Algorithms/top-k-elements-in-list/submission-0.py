class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        lst = []

        for _ in range(k):
            max_item = max(counter, key=counter.get)
            lst.append(max_item)
            del counter[max_item]
        
        return lst