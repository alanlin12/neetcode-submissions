class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_values = {}
        for ch in s:
            seen_values[ch] = 1 + seen_values.get(ch, 0)
        
        for ch in t:
            if ch not in seen_values: return False
            seen_values[ch] -= 1
            if seen_values[ch] == 0: del seen_values[ch]
        
        return not (len(seen_values) > 0)
