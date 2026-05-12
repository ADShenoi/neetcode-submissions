class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for key, val in counter.items():
            freq[val].append(key)
        
        lst = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                lst.append(n)
                if len(lst) == k:
                    return lst
