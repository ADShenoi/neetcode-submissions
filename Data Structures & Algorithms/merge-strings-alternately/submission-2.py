class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0

        chars = []
        while i < len(word1) and j < len(word2):
            chars.extend([word1[i], word2[j]])

            i, j = i+1, j+1
        
        while i < len(word1):
            chars.append(word1[i])
            i += 1
        
        while j < len(word2):
            chars.append(word2[j])
            j += 1
        
        return "".join(chars)