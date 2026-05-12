class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for ele in strs:
            count = [0]*26
            for ch in ele:
                count[ord(ch) - ord('a')] += 1
            
            d[tuple(count)].append(ele)
        
        return list(d.values())