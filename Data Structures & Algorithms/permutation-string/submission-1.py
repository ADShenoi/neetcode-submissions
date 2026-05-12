class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        l = 0
        for r in range(len(s1), len(s2)+1):
            dynamic_counter = Counter(s2[l:r])
            if s1_counter == dynamic_counter :
                return True
            l += 1
        return False

