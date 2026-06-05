class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd, td = {}, {}

        for ele in s:
            sd[ele] = sd.get(ele, 0) + 1
        
        for ele in t:
            td[ele] = td.get(ele, 0) + 1
        
        return sd == td