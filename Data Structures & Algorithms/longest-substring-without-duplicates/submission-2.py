class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        res, curr = 0, 0

        for r in range(len(s)):
            if s[r] not in seen:
                curr += 1
                seen.add(s[r])
                res = max(curr, res)
            
            else:
                while s[r] in seen: 
                    seen.discard(s[l])
                    l += 1
                    curr -= 1
                seen.add(s[r])
                curr += 1
        return res