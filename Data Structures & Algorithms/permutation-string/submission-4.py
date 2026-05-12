class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counter = Counter(s1)
        dynamic_counter = defaultdict(int)
        for i in range(len(s1)):
            dynamic_counter[s2[i]] += 1
        if s1_counter == dynamic_counter :
                return True
        l = 0
        for r in range(len(s1), len(s2)):
            dynamic_counter[s2[r]] += 1
            dynamic_counter[s2[l]] -= 1  
            if dynamic_counter[s2[l]] == 0:
                dynamic_counter.pop(s2[l])    
            
            if s1_counter == dynamic_counter :
                return True      
            l += 1
        return False

