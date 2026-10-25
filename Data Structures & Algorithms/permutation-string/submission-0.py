class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key_word = sorted(s1)
        for l in range(len(s2) - len(s1) + 1):
            if sorted(s2[l: l + len(s1)]) == key_word: return True
        
        return False
