class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = strs.copy()
        for i in range(len(strs)):
            strs[i] = sorted(strs[i])
        
        for i in range(len(strs)):
            strs[i] = ''.join(strs[i])
        
        print(strs)
        d = {}
        for i in range(len(strs)):
            if strs[i] in d:
                d[strs[i]].append(i)
            else:
                d[strs[i]] = [i]
        
        print(d)

        lst = []

        for k, v in d.items():
            for i in range(len(v)):
                v[i] = temp[v[i]]
            lst.append(v)
        
        print(lst)
        return lst